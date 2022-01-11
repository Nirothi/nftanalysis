import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="scoobiekitty2001",
  database="The_Office"
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")