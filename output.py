"""output.py"""

from operator import itemgetter
import mysql.connector
import sys
# connect to my RDS instance
mydb = mysql.connector.connect(
  host="mydatabase.clslb5ktpqun.us-east-1.rds.amazonaws.com",
  user="shudi",
  passwd="shudizhao923",
  database = "mydatabase"
)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from reduce.py
    word, count = line.split()
    try:
        count = int(count)
    except ValueError:        
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    mycursor = mydb.cursor(dictionary=True)
    #insert the output of reducer into the table called Word_Count in my database
    query = "INSERT INTO Word_Count VALUES ('{}', '{}')".format(word, count)
    mycursor.execute(query)
    mydb.commit()












