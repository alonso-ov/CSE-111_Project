import sqlite3
from sqlite3 import Error
import sys
import os

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



def get_user(username, password):

    conn = open_connection(r'test.sqlite3')
    try:
        sql = """
            select *
            from User
            where u_username = '{}'
            and u_password = '{}'
        """.format(username, password)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchone()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

def search_by_no_filter():
    conn = open_connection(r'test.sqlite3')
    try:
        sql = """
            select p_pictureid, p_name, p_agerating, p_genre, p_type, p_releasedate
            from Picture
        """

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()[0:100]

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def search_by_streaming_site(streaming_site):

    conn = open_connection(r'test.sqlite3')
    try:
        sql = """
            select *
            from Picture
            where u_username = '{}'
            and u_password = '{}'
        """.format(streaming_site)

        pass

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')