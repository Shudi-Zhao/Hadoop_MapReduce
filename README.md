# Hadoop MapReduce(Word Count Project)

## Project Overview
This project demonstrates the use of Hadoop MapReduce for solving a word count problem. The goal is to process a large text file and count the frequency of each word. This project involves setting up and executing MapReduce processes in Python, running them on an EC2 instance, and storing the output in an RDS MySQL database.

## Procedures:
1. **Data Source**:  
   The text used for this word count problem is *Treasure Island* by Robert Louis Stevenson, sourced from [Project Gutenberg](https://www.gutenberg.org/).
   
2. **MapReduce Program**:  
   Two Python scripts were developed to simulate the MapReduce process:
   - `map.py`: The Mapper function processes input by splitting lines of text and emitting word-count pairs.
   - `reduce.py`: The Reducer function aggregates word counts across multiple records and outputs the total count for each word.

3. **Execution on EC2**:  
   The program was executed on an Amazon EC2 instance running Ubuntu. The command used to simulate the MapReduce process was as follows:
   
   ```bash
   cat TreasureIsland.txt | python map.py | sort -k1,1 | python reduce.py | python output.py
