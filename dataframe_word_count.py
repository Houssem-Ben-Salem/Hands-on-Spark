# dataframe_word_count.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as func

# Create a Spark session
spark = SparkSession.builder.appName("WordCountDF").getOrCreate()

# Read each line of my book into a dataframe
inputDF = spark.read.text("file:///home/hous/Desktop/pyspark/book.txt")  # Update the path

# Split using a regular expression that extracts words
words = inputDF.select(func.explode(func.split(inputDF.value, "\\W+")).alias("word"))

# Filter out empty words
nonEmptyWords = words.filter(words.word != "")

# Normalize everything to lowercase
lowercaseWords = nonEmptyWords.select(func.lower(nonEmptyWords.word).alias("word"))

# Count up the occurrences of each word
wordCounts = lowercaseWords.groupBy("word").count()

# Sort by counts
wordCountsSorted = wordCounts.sort("count")

# Show the results
wordCountsSorted.show(wordCountsSorted.count())

# Stop the session
spark.stop()