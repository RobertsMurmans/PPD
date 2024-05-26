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
    cur = con.cursor()

    cur.execute("   SELECT Password FROM Users WHERE Username = %s   ", (username, ))

    Password = cur.fetchall()

    if Password == None:
        print(username, " does not exists")
        return False
    
    Password = Password[0][0]

    cur.close()
    con.commit()
    con.close()

    print("With password tried: ", password, " and ", Password)
    
    if password == Password:
        print("Connection success from", username)
        return True
    print("Connection fail from", username)
    return False

def getID(username):
    con = connectToSQL()
    cur = con.cursor()

    cur.execute("   SELECT UserID FROM Users Where Username = %s   ", (username, ))

    userID = cur.fetchone()

    cur.close()
    con.commit()
    con.close()

    return userID
