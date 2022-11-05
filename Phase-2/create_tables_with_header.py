import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("Opening database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("OpenConnectionSuccess!")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("CloseConnectionSuccess!")
    except Error as e:
        print(e)


def createTables(_conn):
    print("Create tables")

    try:
        
        # DECIMAL(20,0) = 20 digits before decimal point and 0 digits after decimal point
        sql =  """
            CREATE TABLE IF NOT EXISTS USER  (
            u_id DECIMAL(10,0) NOT NULL,
            u_username CHAR(2) NOT NULL,
            u_email CHAR(40) NOT NULL,
            u_firstname CHAR(30) NOT NULL,
            u_lastname CHAR(30) NOT NULL,
            u_preferredstreamsite CHAR(15) NOT NULL
            )
        """
        #Notes: https://linuxhint.com/create-table-in-sqlite-using-if-not-exists-statement/

        _conn.execute(sql)
        print("users created")

        sql = """
            CREATE TABLE IF NOT EXISTS User_Review (
            p_id STRING(8) NOT NULL,
            u_id DECIMAL(10,0) NOT NULL,
            r_comment CHAR(10000) NOT NULL,
            r_userrating DECIMAL(1,1) NOT NULL,
            r_date CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("user_review created")

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
        print("picture created")

        sql = """
            CREATE TABLE IF NOT EXISTS Media_Watch_List (           
            u_id DECIMAL(10,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            w_watchstatus CHAR(20) NOT NULL,
            w_completiondate CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("media_watch_list created")

        sql = """
            CREATE TABLE Streaming_Availibility (            
            sa_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            sa_neflix BOOLEAN NOT NULL CHECK (sa_neflix IN (0, 1)),
            sa_hulu BOOLEAN NOT NULL CHECK (sa_hulu IN (0, 1)),
            sa_primevid BOOLEAN NOT NULL CHECK (sa_primevid IN (0, 1)),
            sa_disney+ BOOLEAN NOT NULL CHECK (sa_disneyplus IN (0, 1)) 
            )
        """
        #Notes: https://stackoverflow.com/questions/843780/store-boolean-value-in-sqlite

        _conn.execute(sql)
        print("streaming_availibility created")

        sql = """
            CREATE TABLE Public_Ratings (            
            pr_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            pr_RTrating DECIMAL(2,1) NOT NULL,
            pr_IMDbrating DECIMAL(2,3)) NOT NULL
            )
        """
        _conn.execute(sql)
        print("public_ratings created")

        sql = """
            CREATE TABLE Cast_Member (
            ca_id DECIMAL(8,0) NOT NULL,
            ca_name CHAR(80) NOT NULL
            )
        """
        _conn.execute(sql)
        print("cast_member created")

        sql = """
            CREATE TABLE Media_Cast_Member (
            p_id STRING(8) NOT NULL,
            ca_id DECIMAL(8,0) NOT NULL,
            mc_role CHAR(8) NOT NULL
            )
        """
        _conn.execute(sql)
        print("media_cast_member created")
       
        _conn.commit()
        print("CreationTablesSuccess!") #commiting worked  
         
    except Error as e:
        _conn.rollback()
        print(e)

def dropTables(_conn):
    print("Drop Tables")

    try:
        sql = "DROP TABLE IF EXISTS Picture"
        sql = "DROP TABLE IF EXISTS Streaming_Availability"
        sql = "DROP TABLE IF EXISTS Public_Ratings"
        sql = "DROP TABLE IF EXISTS Cast_Member"
        sql = "DROP TABLE IF EXISTS Media_Cast_Member"

        _conn.execute(sql)
        _conn.commit()
        print("DropTablesSuccess!")
    
    except Error as e:
        print(e)
        _conn.rollback()
        print(e) 


def main():
    database = r"db.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn) #should drop tables where data is populated from csv files
        createTables(conn) #creating tables once again where data is populated from csv files, but the other tables should be kept

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
