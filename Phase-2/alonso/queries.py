import sqlite3
from sqlite3 import Error
import sys, os

'''
1. create a user
2. edit a user
3. delete user
4. create review
5. edit review
6. delete review
7. create picture
8. edit picture
9. delete picture
10. create cast member
11. edit cast member
12. delete cast member
13. create streaming availibility
14. edit streaming availibility
15. delete streaming availibility
16. search by streaming availibility
17. search by cast member
18. search by rating
19. search by genre
20. search by picture
'''

def openConnection(_dbFile):
    print("Opening database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Connection opened...")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("Connection closed...")
    except Error as e:
        print(e)

def createUser(_conn, u_email, u_username, u_password, u_firstname, u_lastname, u_referredstreamsite):
    try:

        sql = """
            select count(*)
            from User
        """
        cur = _conn.cursor()

        cur.execute(sql)

        User_len = cur.fetchone()[0]

        new_u_id = User_len

        new_user = [(new_u_id, u_email, u_username, u_password, u_firstname, u_lastname, u_referredstreamsite)]

        sql = "INSERT INTO User VALUES(?, ?, ?, ?, ?, ?, ?)"

        _conn.executemany(sql,  new_user)   
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e) 

def editUser(_conn, u_userid, u_email, u_username, u_password, u_firstname, u_lastname, u_peferredstreamsite):
    
    try:
        sql = """
        UPDATE User
        SET u_email={}, u_username={}, u_password={}, u_firstname={}, u_lastname, u_preferredstreamite={},
        where u_userid = {}
        """.format(u_email, u_username, u_password, u_firstname, u_lastname, u_peferredstreamsite, u_userid)

        _conn.execute(sql)
        _conn.commit()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        _conn.rollback()

def deleteUser(_conn, u_id):
    
    try:
        sql = """
            delete from user
            where u_userid = {}
        """.format(u_id)

        _conn.execute(sql)
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)

def addPersonalRating(_conn, p_id, u_id, r_comment, r_userrating, r_date):
    try:
        sql = """
            select count(*)
            from User_Review
        """
        cur = _conn.cursor()

        cur.execute(sql)

        User_Review_len = cur.fetchone()[0]

        new_r_id = User_Review_len

        new_review = (new_r_id, p_id, u_id, r_comment, r_userrating, r_date)

        sql = "INSERT INTO User_Review VALUES(?, ?, ?, ?, ?, ?)"

        _conn.execute(sql, new_review)
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)

def deletePersonalRating(_conn, r_id):
    try:
        sql = """
            delete from User_Review
            where ur_reviewid = {}
        """.format(r_id)

        _conn.execute(sql)
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)


def main():
    database = r"test.sqlite3"
    # create a database connection
    conn = openConnection(database)

    #create dummy user
    #createUser(conn, 'alonso@email.com', 'alonso123', '123', 'alonso', 'ortiz', 'netflix')
    #deleteUser(conn, 5)
    editUser(conn, 0, 'alonso1234', '1234', 'alonso@email.com', 'alonsoo', 'ortizz', 'hulu')

    #add dummy rating
    #addPersonalRating(conn, 'tm204541', 1, 'mid movie', 5, '2022-11-06')
    #deletePersonalRating(conn, 2)




    closeConnection(conn, database)

if __name__ == '__main__':
    main()