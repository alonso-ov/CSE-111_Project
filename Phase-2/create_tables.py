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


def createTables(_conn):
    print("------ Creating tables ------")

    _conn.execute("BEGIN")
    try:
        
        # DECIMAL(20,0) = 20 digits before decimal point and 0 digits after decimal point
        sql =  """
            CREATE TABLE User  (
            u_id DECIMAL(10,0) NOT NULL,
            u_username CHAR(2) NOT NULL,
            u_email CHAR(40) NOT NULL,
            u_firstname CHAR(30) NOT NULL,
            u_lastname CHAR(30) NOT NULL,
            u_preferredstreamsite CHAR(15) NOT NULL
            )
        """

        _conn.execute(sql)
        print("Users created")

        sql = """
            CREATE TABLE User_Review (
            p_id STRING(8) NOT NULL,
            u_id DECIMAL(10,0) NOT NULL,
            r_comment CHAR(10000) NOT NULL,
            r_userrating DECIMAL(1,1) NOT NULL,
            r_date CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("User_Review created")

        sql = """
            CREATE TABLE Picture (
            p_id STRING(8) NOT NULL,
            p_name DECIMAL(100,0) NOT NULL,
            p_releasedate CHAR(4) NOT NULL,
            p_agerating CHAR(5) NOT NULL,
            p_type CHAR(5) NOT NULL,
            p_genre CHAR(100) NOT NULL
            )
        """
        _conn.execute(sql)
        print("Picture created")

        sql = """
            CREATE TABLE Media_Watch_List (           
            u_id DECIMAL(10,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            w_watchstatus CHAR(20) NOT NULL,
            w_completiondate CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("Media_Watch_List created")

        sql = """
            CREATE TABLE Streaming_Availibility (            
            sa_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            sa_neflix BOOLEAN NOT NULL CHECK (sa_neflix IN (0, 1)),
            sa_hulu BOOLEAN NOT NULL CHECK (sa_hulu IN (0, 1)),
            sa_primevid BOOLEAN NOT NULL CHECK (sa_primevid IN (0, 1)),
            sa_disney BOOLEAN NOT NULL CHECK (sa_disney IN (0, 1)) 
            )
        """

        _conn.execute(sql)
        print("Streaming_Availibility created")

        sql = """
            CREATE TABLE Public_Ratings (            
            pr_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            pr_RTrating DECIMAL(2,1) NOT NULL,
            pr_IMDbrating DECIMAL(2,3) NOT NULL
            )
        """
        _conn.execute(sql)
        print("Public_Ratings created")

        sql = """
            CREATE TABLE Cast_Member (
            ca_id DECIMAL(8,0) NOT NULL,
            ca_name CHAR(80) NOT NULL
            )
        """
        _conn.execute(sql)
        print("Cast_Member created")

        sql = """
            CREATE TABLE Media_Cast_Member (
            p_id STRING(8) NOT NULL,
            ca_id DECIMAL(8,0) NOT NULL,
            mc_role CHAR(8) NOT NULL
            )
        """
        _conn.execute(sql)
        print("Media_Cast_Member created")
       
        _conn.commit()
        print("------ Successfully created all tables ------\n") #commiting worked  
         
    except Error as e:
        _conn.rollback()
        print(e)

def dropTables(_conn):
    print("------ Drop Tables ------")

    try:
        sql = "DROP TABLE IF EXISTS Picture"
        _conn.execute(sql)
        print('Picture deleted')


        sql = "DROP TABLE IF EXISTS Streaming_Availability"
        _conn.execute(sql)
        print('Streaming_Availability deleted')


        sql = "DROP TABLE IF EXISTS Public_Ratings"
        _conn.execute(sql)
        print('Public_Ratings deleted')


        sql = "DROP TABLE IF EXISTS Cast_Member"
        _conn.execute(sql)
        print('Cast_Member deleted')


        sql = "DROP TABLE IF EXISTS Media_Cast_Member"
        _conn.execute(sql)
        print('Media_Cast_Member deleted')

        
        _conn.commit()
        print("------  Successfull dropped all tables ------\n")
    
    except Error as e:
        print(e)
        _conn.rollback()
        print(e) 

def populatePicture(_conn):
    pass


def main():
    database = r"test.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populatePicture(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()