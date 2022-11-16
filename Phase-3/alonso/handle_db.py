import sqlite3
from sqlite3 import Error

def open_connection(_dbFile):
    print("Opening database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Connection opened...")
    except Error as e:
        print(e)

    return conn

def close_connection(_conn, _dbFile):
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("Connection closed...")
    except Error as e:
        print(e)