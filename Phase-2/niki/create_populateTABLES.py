import sqlite3
from sqlite3 import Error
import csv


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
            CREATE TABLE IF NOT EXISTS User  (
            u_id DECIMAL(10,0) NOT NULL,
            u_username CHAR(20) NOT NULL,
            u_passcode CHAR(25) NOT NULL,
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
            r_id DECIMAL(5,0) NOT NULL,
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
            CREATE TABLE IF NOT EXISTS Picture (
            p_id STRING(8) NOT NULL,
            p_name DECIMAL(100,0) NOT NULL,
            p_type CHAR(5) NOT NULL,
            p_releasedate CHAR(4) NOT NULL,
            p_agerating CHAR(5) NOT NULL,
            p_genre CHAR(100) NOT NULL
            )
        """
        _conn.execute(sql)
        print("picture created")

        sql = """
            CREATE TABLE IF NOT EXISTS Media_Watch_List (  
            w_id DECIMAL(5,0) NOT NULL,         
            u_id DECIMAL(10,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            w_watchstatus CHAR(20) NOT NULL,
            w_completiondate CHAR(10) NOT NULL
            )
        """
        _conn.execute(sql)
        print("media_watch_list created")

        sql = """
            CREATE TABLE IF NOT EXISTS Streaming_Availibility (            
            sa_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            sa_neflix BOOLEAN NOT NULL CHECK (sa_neflix IN (0, 1)),
            sa_hulu BOOLEAN NOT NULL CHECK (sa_hulu IN (0, 1)),
            sa_primevid BOOLEAN NOT NULL CHECK (sa_primevid IN (0, 1)),
            sa_disneyplus BOOLEAN NOT NULL CHECK (sa_disneyplus IN (0, 1)) 
            )
        """
        #Notes: https://stackoverflow.com/questions/843780/store-boolean-value-in-sqlite

        _conn.execute(sql)
        print("streaming_availibility created")

        sql = """
            CREATE TABLE IF NOT EXISTS Public_Ratings (            
            pr_id DECIMAL(5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            pr_imdb DECIMAL(2,3) NOT NULL,
            pr_tmdb DECIMAL(2,3) NOT NULL
            )
        """
        _conn.execute(sql)
        print("public_ratings created")

        sql = """
            CREATE TABLE IF NOT EXISTS Cast_Member (
            ca_id DECIMAL(8,0) NOT NULL,
            ca_name CHAR(80) NOT NULL
            )
        """
        _conn.execute(sql)
        print("cast_member created")

        sql = """
            CREATE TABLE IF NOT EXISTS Media_Cast_Member (
            mcm_id DECIMAL (5,0) NOT NULL,
            p_id STRING(8) NOT NULL,
            ca_id DECIMAL(8,0) NOT NULL,
            mcm_role CHAR(8) NOT NULL
            )
        """
        _conn.execute(sql)
        print("media_cast_member created")
       
        _conn.commit()
        print("CreationTablesSuccess!") #commiting worked  
         
    except Error as e:
        _conn.rollback()
        print(e)
        
def  populateTables(_conn):
    
    print("Populate table")
    try:
              
        #load picture.csv data into Picture table
        file = open('picture.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO Picture (p_id, p_name, p_type, p_releasedate, p_agerating, p_genre) VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(insert_records, contents)
        _conn.commit()
        
         #load streaming_availibility.csv data into Streaming_Availibility table
        file = open('streaming_availability.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO Streaming_Availibility (sa_id, p_id, sa_neflix, sa_hulu, sa_primevid, sa_disneyplus) VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(insert_records, contents)
        _conn.commit()
        
        #load public_ratings.csv data into Public_Ratings table
        file = open('public_ratings.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO Public_Ratings (pr_id, p_id, pr_imdb, pr_tmdb) VALUES(?, ?, ?, ?)"
        _conn.executemany(insert_records, contents)
        _conn.commit()
        
        #load cast_member.csv data into Cast_Member table
        file = open('cast_member.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO Cast_Member (ca_id, ca_name) VALUES(?, ?)"
        _conn.executemany(insert_records, contents)
        _conn.commit()
        
        #load media_cast_member.csv data into Media_Cast_Member table
        file = open('media_cast_member.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO Media_Cast_Member (mcm_id, ca_id, p_id, mcm_role) VALUES(?, ?, ?, ?)"
        _conn.executemany(insert_records, contents)
        _conn.commit()
        
        #inserting dummy values into User table 
        userrows = [
            (0,'jellybean','Lucky!ghdf#','jennysmith1@gmail.com', 'Jenny', 'Smith', 'Netflix'),
            (1,'frenzzy','HFfgdr$33', 'cindyyyyyy@yahoo.com', 'Cindy', 'Lin', 'Netflix'),
            (2,'waterdrop','HFgfege$5', 'b0bSchwartz@gmail.com', 'Bob', 'Schwartz', 'Amazon Prime'),
            (3,'questseeker','dfgh@arrtFlow', 'Marc0G0mez@hotmail.com', 'Marco', 'Gomez', 'Hulu'),
            (4,'foodieaddict','Fsddhltyy%tu', 'katerin@gmail.com', 'Kate', 'Rin', 'Disney+')
        ]
        sql = "INSERT INTO User VALUES(?, ?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql,  userrows)   
        _conn.commit()
        
        #inserting dummy values into Media_Watch_List table, manual insert 
        userrows = [
            (0, 0,'tm84618', 'watching', ''),
            (1, 0,'tm69997', 'watch later', ''),
            (2, 3,'tm204541', 'completed', '2021-06-22'),
            (3, 3,'tm100027', 'watch later', ''),
            (4, 1,'ts20681', 'completed', '2019-08-17')
        ]
        sql = "INSERT INTO Media_Watch_List VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql,  userrows)   
        _conn.commit()
        
        #inserting dummy values into User_Review table
        userrows = [
            (0, 'tm204541', 3,'liked this', 4, '2021-06-24'),
            (1, 'ts20681', 1,'did not like this', 1.5, '2019-08-25')
        ]
        sql = "INSERT INTO User_Review VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql,  userrows)   
        _conn.commit()
        
             
    except Error as e:
        _conn.rollback()
        print(e)

'''
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
'''

def main():
    database = r"db.sqlite3"
    # create a database connection
    conn = openConnection(database)
    
    dataload = True
    
    with conn:
        createTables(conn) #creating tables once again where data is populated from csv files, but the other tables should be kept
        #dropTables(conn) #should drop tables where data is populated from csv files
    
    if (dataload == True):
        populateTables(conn)   
    
    closeConnection(conn, database)

if __name__ == '__main__':
    main()