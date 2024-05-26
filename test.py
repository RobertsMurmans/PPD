import mysql.connector as co
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_Host')
port = os.getenv('DB_Port')
name = os.getenv('DB_Name')
password = os.getenv('DB_Password')
database = os.getenv('DB')

connection = None
print("ted")
connection = co.connect(host=host, port=port, user=name, passwd=password, database=database)
print("conected")
cur = connection.cursor()

cur.execute("SELECT * FROM Users")

print(cur.fetchall())

cur.close()
connection.commit()
connection.close()