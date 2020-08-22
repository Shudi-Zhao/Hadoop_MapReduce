# Hadoop MapReduce Homework
Word count problem using Hadoop map reduce.

Procedures:

1. I chose a book called Treasure Island from Project Gutenberg: https://www.gutenberg.org/ (Links to an external site.)
2. I wrote a Hadoop MapReduce program in python(map.py, reduce.py) to calculate the word count.
3. I Simulated the MapReduce steps on EC2 ubuntu server.
4. I wrote my output.py to store the output of the reduce.py, and then insert this data into my RDS instance. (Used the following command: cat TreasureIsland.txt | python map.py | sort -k1,1 | python reduce.py | python output.py)
