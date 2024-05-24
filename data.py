import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('DB_Adress')
name = os.getenv('DB_Name')
password = os.getenv('DB_Password')
database = os.getenv('DB')

mydb = mysql.connector.connect(host=host, user=name, password=password, database=database)

def confirmPass(userID, password):
    
    return True

