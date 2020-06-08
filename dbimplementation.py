import mysql.connector

con = mysql.connector.connect(
user = "dipen044",
password = "pass",
host = "108.167.140.122",
database = "myfirstdb"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")