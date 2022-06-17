import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jennifer1992"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
