import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("Opening database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)


def createTables(_conn):
    print("Create tables")

    _conn.execute("BEGIN")
    try:

        sql = """
            CREATE TABLE Users(

            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE User_Review(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Picture(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Media_Watch_List(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Streaming_Availibility(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Public_Ratings(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Media_Cast_Member(
                
            )
        """

        _conn.execute(sql)

        sql = """
            CREATE TABLE Cast_Member(
                
            )
        """

        _conn.execute(sql)


        _conn.execute("COMMIT")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def dropTables(_conn):
    print("Drop Tables")

    sql = """
        DROP TABLE warehouse
    """

    _conn.execute(sql)
    _conn.commit()


def main():
    database = r"db.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()