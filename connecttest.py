import mysql.connector

mydb = mysql.connector.connect(
  host="db-cclpro.c7g86aoqaeg1.us-east-1.rds.amazonaws.com",
  user="admin",
  port=3306,
  password="12345678"
)

if(mydb):
    print("Connecting to")
else:   
    print("No connection")