#para instalar o mysql connector
# pip install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="forge"
)

cursor = conn.cursor()

