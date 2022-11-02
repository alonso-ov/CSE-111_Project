import sqlite3
from sqlite3 import Error
import os

# Creates a relative path 
relativeDir = os.path.dirname(__file__)
databasePath = os.path.join(relativeDir, 'db.sqlite3')

def createConnection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    

if __name__ == '__main__':
    createConnection(databasePath)