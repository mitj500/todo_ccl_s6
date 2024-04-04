import mysql.connector

mydb = mysql.connector.connect(
  host="database-1.c7g86aoqaeg1.us-east-1.rds.amazonaws.com",
  user="admin",
  port=3306,
  password="12345678",
  database="db_ccl"
)

if(mydb):
    print("Connecting to")
else:   
    print("No connection")