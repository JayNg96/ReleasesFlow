import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS internship_data")


my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)


mydb.close()