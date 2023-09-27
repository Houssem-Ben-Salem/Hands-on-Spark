# Hands-on-Spark

This repository contains Python and shell script files for running various word count and text processing operations using PySpark. Below are the descriptions of each file and instructions on how to use them.

## Files Description

1. **book.txt**:  
   The input text file on which word count and text processing operations are performed.

2. **word_count.py**:  
   A PySpark script for counting the occurrence of each distinct word in 'book.txt'.

3. **normalized_word_count.py**:  
   A PySpark script similar to 'word_count.py', but it converts all words to lowercase and removes non-word characters before counting.

4. **sorted_word_count.py**:  
   This script sorts the words from 'normalized_word_count.py' in ascending order based on their counts.

5. **dataframe_word_count.py**:  
   A PySpark script that uses DataFrames and SQL functions to perform the word count operation, providing a different approach from the RDD-based methods used in the previous scripts.

6. **run_word_count.sh**:  
   A Bash script to execute 'word_count.py' using spark-submit.

7. **run_normalized_word_count.sh**:  
   A Bash script to execute 'normalized_word_count.py' using spark-submit.

8. **run_sorted_word_count.sh**:  
   A Bash script to execute 'sorted_word_count.py' using spark-submit.

9. **run_dataframe_word_count.sh**:  
   A Bash script to execute 'dataframe_word_count.py' using spark-submit.

## How to Change File Permissions

Before running the shell script files, you need to change their permissions to make them executable. You can do this using the `chmod` command in your terminal. For example, to change the permissions of 'run_word_count.sh':

```bash
chmod +x run_word_count.sh
```

Repeat this process for all the `.sh` files.

## Paths to Update

In each PySpark `.py` file, ensure to update the path of the 'book.txt' to where it is located on your local machine. For example, in 'word_count.py':

```python
input = sc.textFile("file:///your/path/to/book.txt")
```

Replace `"file:///your/path/to/book.txt"` with the actual path to your 'book.txt'.

## How to Run the Scripts

Each `.sh` file is associated with a `.py` file. To run a PySpark script, execute the corresponding `.sh` file. For example, to run 'word_count.py', execute 'run_word_count.sh' as follows:

```bash
./run_word_count.sh
```

Ensure you are in the correct directory, or provide the path to the `.sh` file.

## Note

Ensure that Spark is installed and properly configured on your machine. Update the SPARK_HOME variable in each `.sh` file to point to your Spark installation directory, for example:

```bash
export SPARK_HOME=/path/to/your/spark/installation
```

Replace `/path/to/your/spark/installation` with the actual path where Spark is installed on your system.
