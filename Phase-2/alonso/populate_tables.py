import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("------ Opening database: ", _dbFile, ' ------')

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("------ Database successfully opened ------\n")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("\nConnection closed....")
    except Error as e:
        print(e)

def populate(_conn):
    print("------ Populating Tables ------")

    try:
        sql = """
            .mode "csv"
            .seperator ","
        """
        _conn.execute(sql)
        print('Picture populated')
        
        _conn.commit()
        print("------  Successfully populated all tables ------\n")
    
    except Error as e:
        print(e)
        _conn.rollback()
        print(e) 


def main():
    database = r"test.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        populate(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()