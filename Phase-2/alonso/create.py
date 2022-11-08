import sqlite3
from sqlite3 import Error
import sys, os


def openConnection(_dbFile):
    print("\n{:*^60}\n".format(("Opening database: " + _dbFile)))

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("\n{:*^60}\n".format("Database successfully opened"))
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("\n{:*^60}\n".format(("Closing database: " + _dbFile)))

    try:
        _conn.close()
        print("\nConnection closed....")
    except Error as e:
        print(e)


def createTables(_conn):
    print("\n{:-^60}\n".format("Creating tables"))

    _conn.execute("BEGIN")
    try:

        print("Creating table:")

        sql =  """
            CREATE TABLE Admin  (
            a_adminid INTEGER NOT NULL,
            a_userid INTEGER NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Admin")


        sql =  """
            CREATE TABLE User  (
            u_userid INTEGER NOT NULL,
            u_email VARCHAR NOT NULL,
            u_password VARCHAR NOT NULL,
            u_username VARCHAR NOT NULL,
            u_firstname VARCHAR NOT NULL,
            u_lastname VARCHAR NOT NULL,
            u_preferredstreamsite CHAR(15) NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Users")


        sql = """
            CREATE TABLE User_Review (
            ur_pictureid STRING(8) NOT NULL,
            ur_userid INTEGER NOT NULL,
            ur_comment CHAR(10000) NOT NULL,
            ur_userrating DECIMAL(1,1) NOT NULL,
            ur_date CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("-User_Review")


        sql = """
            CREATE TABLE Picture (
            p_pictureid STRING(8) NOT NULL,
            p_name VARCHAR NOT NULL,
            p_releasedate CHAR(4) NOT NULL,
            p_agerating CHAR(5) NOT NULL,
            p_genre CHAR(5) NOT NULL,
            p_type CHAR(100) NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Picture")


        sql = """
            CREATE TABLE Media_Watch_List (           
            mwl_userid INTEGER NOT NULL,
            mwl_id STRING(8) NOT NULL,
            mwl_watchstatus VARCHAR NOT NULL,
            mwl_completiondate VARCHAR NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Media_Watch_List")


        sql = """
            CREATE TABLE Streaming_Availability (            
            sa_said INTEGER NOT NULL,
            sa_pictureid STRING(8) NOT NULL,
            sa_netflix BOOLEAN NOT NULL CHECK (sa_netflix IN (0, 1)),
            sa_hulu BOOLEAN NOT NULL CHECK (sa_hulu IN (0, 1)),
            sa_primevid BOOLEAN NOT NULL CHECK (sa_primevid IN (0, 1)),
            sa_disneyplus BOOLEAN NOT NULL CHECK (sa_disneyplus IN (0, 1)) 
            )
        """
        _conn.execute(sql)
        print("-Streaming_Availability")


        sql = """
            CREATE TABLE Public_Ratings (            
            pr_ratingid INTEGER NOT NULL,
            pr_pictureid STRING(8) NOT NULL,
            pr_RTrating DECIMAL(2,1) NOT NULL,
            pr_IMDbrating DECIMAL(2,3) NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Public_Ratings")

        sql = """
            CREATE TABLE Cast_Member (
            cm_cmid INTEGER NOT NULL,
            cm_personid INTEGER NOT NULL,
            cm_name VARCHAR NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Cast_Member")

        sql = """
            CREATE TABLE Media_Cast_Member (
            mcm_mcmid INTEGER NOT NULL,
            mcm_pictureid STRING(8),
            mcm_personid INTEGER,
            mcm_role VARCHAR NOT NULL
            )
        """
        _conn.execute(sql)
        print("-Media_Cast_Member")
       
        _conn.commit()
        print("\n{:-^60}\n".format("Successfully created all tables"))
         
    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        _conn.rollback()

def dropTables(_conn):
    print("\n{:-^60}\n".format("Dropping tables"))

    try:
        print("Deleting table:")

        sql = "DROP TABLE IF EXISTS Admin"
        _conn.execute(sql)
        print('-Admin')

        sql = "DROP TABLE IF EXISTS User"
        _conn.execute(sql)
        print('-User')

        sql = "DROP TABLE IF EXISTS User_Review"
        _conn.execute(sql)
        print('-User_Review')

        sql = "DROP TABLE IF EXISTS Picture"
        _conn.execute(sql)
        print('-Picture')

        sql = "DROP TABLE IF EXISTS Media_Watch_List"
        _conn.execute(sql)
        print('-Media_Watch_List')


        sql = "DROP TABLE IF EXISTS Streaming_Availability"
        _conn.execute(sql)
        print('-Streaming_Availability')


        sql = "DROP TABLE IF EXISTS Public_Ratings"
        _conn.execute(sql)
        print('-Public_Ratings')


        sql = "DROP TABLE IF EXISTS Cast_Member"
        _conn.execute(sql)
        print('-Cast_Member')


        sql = "DROP TABLE IF EXISTS Media_Cast_Member"
        _conn.execute(sql)
        print('-Media_Cast_Member')

        
        _conn.commit()
        print("\n{:-^60}\n".format("Successfully dropped all tables"))
    
    except Error as e:
        print(e)
        _conn.rollback()
        print(e) 


def main():
    database = r"test.sqlite3"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()