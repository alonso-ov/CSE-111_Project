import sqlite3
from sqlite3 import Error
import csv

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
        file = open("copies/picture.csv")
        contents = csv.reader(file)
        insert_statement = "INSERT INTO Picture (p_pictureid, p_name, p_type, p_releasedate, p_agerating, p_genre) VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(insert_statement, contents)
        _conn.commit()
        print('-Picture')

        file = open("copies/cast_member_mod.csv")
        contents = csv.reader(file)
        insert_statement = "INSERT INTO Cast_Member (cm_personid, cm_name, cm_cmid) VALUES(?, ?, ?)"
        _conn.executemany(insert_statement, contents)
        _conn.commit()
        print('-Cast_Member')

        file = open("copies/media_cast_member.csv")
        contents = csv.reader(file)
        insert_statement = "INSERT INTO Media_Cast_Member (mcm_mcmid, mcm_personid, mcm_pictureid, mcm_role) VALUES(?, ?, ?, ?)"
        _conn.executemany(insert_statement, contents)
        _conn.commit()
        print('-Media_Cast_Member')

        file = open("copies/public_ratings.csv")
        contents = csv.reader(file)
        insert_statement = "INSERT INTO Public_Ratings (pr_ratingid, pr_pictureid, pr_RTrating, pr_IMDbrating) VALUES(?, ?, ?, ?)"
        _conn.executemany(insert_statement, contents)
        _conn.commit()
        print('-Public_Ratings')

        file = open("copies/streaming_availability.csv")
        contents = csv.reader(file)
        insert_statement = "INSERT INTO Streaming_Availability (sa_said, sa_pictureid, sa_netflix, sa_hulu, sa_primevid, sa_disneyplus) VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(insert_statement, contents)
        _conn.commit()
        print('-Streaming_Availability')

        
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