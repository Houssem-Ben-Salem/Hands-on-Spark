#!/bin/bash

# Set Spark's home directory based on the location of spark-submit
export SPARK_HOME=/opt/spark

# Run the PySpark script
$SPARK_HOME/bin/spark-submit dataframe_word_count.py
