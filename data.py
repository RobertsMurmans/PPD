import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

adress = os.getenv('DB_Adress')
host = os.getenv('DB_Host')
port = os.getenv('DB_Port')
name = os.getenv('DB_Name')
password = os.getenv('DB_Password')
database = os.getenv('DB')


def connectToSQL():
    connection = mysql.connector.connect(host=host, port=port, user=name, password=password, database=database)
    return connection


def confirmPass(username, password):
    con = connectToSQL()
    print("connected")
    cur = con.cursor()

    cur.execute("   SELECT Password FROM Users WHERE Username = %s   ", (username, ))
    con.commit()

    Password = cur.fetchall()

    cur.close()
    con.close()

    if password == Password:
        print("Connection success from", username)
        return True
    print("Connection fail from", username)
    return False
