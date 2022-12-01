import sqlite3
from sqlite3 import Error
import sys
import os

'''
    This file will handle our queries

    Call a function and data from query will be gathered
'''

def open_connection(_dbFile):
    #print("Opening database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        #print("Connection opened...")
    except Error as e:
        print(e)

    return conn

def close_connection(_conn, _dbFile):
    #print("Closing database: ", _dbFile)

    try:
        _conn.close()
        #print("Connection closed...")
    except Error as e:
        print(e)


'''
    Get all user info stored in database

    :param1: name of user
    :param2: password of user
    :return: all user info (email, firstname, etc)
'''
def get_user_info(username, password):

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

'''
    Get everything from every picture

    :return: all available data from every picture
'''
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

'''
    TODO: finish
'''
def search_by_streaming_site(streaming_sites):

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

'''
    :param1: picture identifier
    :return: all columns related to that specified picture
'''
def get_picture_info(picture_id):

    conn = open_connection(r'test.sqlite3')


    try:
        sql = """
            select *
            from Picture
            where p_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all available streaming platforms
'''
def get_streaming_availability(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select sa_netflix, sa_hulu, sa_primevid, sa_disneyplus
            from Streaming_Availability
            where sa_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all public ratings
'''
def get_public_ratings(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select pr_RTrating, pr_IMDbrating
            from Public_Ratings
            where pr_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all user reviews
'''
def get_user_reviews(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select u_username, ur_comment, ur_userrating, ur_date
            from User_Review, User
            where ur_pictureid == '{}'
                and ur_userid = u_userid
        """.format(picture_id)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: picture identifier
    :return: all cast members and their roles
'''
def get_media_cast_members(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select mcm_role, cm_name
            from Media_Cast_Member, Cast_Member
            where mcm_personid = cm_personid
                and mcm_pictureid = '{}'
            group by mcm_role, cm_name
        """.format(picture_id)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')


'''
    Get everything from every picture

    :return: all available data from every picture
'''
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

'''
    TODO: finish
'''
def search_by_streaming_site(streaming_sites):

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

'''
    :param1: picture identifier
    :return: all columns related to that specified picture
'''
def get_picture_info(picture_id):

    conn = open_connection(r'test.sqlite3')


    try:
        sql = """
            select *
            from Picture
            where p_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all available streaming platforms
'''
def get_streaming_availability(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select sa_netflix, sa_hulu, sa_primevid, sa_disneyplus
            from Streaming_Availability
            where sa_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all public ratings
'''
def get_public_ratings(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select pr_RTrating, pr_IMDbrating
            from Public_Ratings
            where pr_pictureid = '{}'
        """.format(picture_id)

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

'''
    :param1: picture identifier
    :return: all user reviews
'''
def get_user_reviews(picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select u_username, ur_comment, ur_userrating, ur_date
            from User_Review, User
            where ur_pictureid == '{}'
                and ur_userid = u_userid
        """.format(picture_id)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: user input
    :return: all movies with specified release year
'''
def search_by_release_year(user_input):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select p_pictureid, p_name, p_agerating, p_genre, p_type, p_releasedate
            from Picture
            where p_releasedate like '%{}%'
            limit 100
        """.format(user_input)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: user input
    :return: all movies with similar name as specified in user input
'''
def search_by_picture_name(user_input):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select p_pictureid, p_name, p_agerating, p_genre, p_type, p_releasedate
            from Picture
            where p_name like '%{}%'
            limit 50
        """.format(user_input)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: user input
    :return: all movies with specified cast member name
'''
def search_by_cast_member_name(user_input):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select p_pictureid, p_name, p_agerating, p_genre, p_type, p_releasedate
            from Picture, Media_Cast_Member, Cast_Member
            where p_pictureid = mcm_pictureid
                and mcm_personid = cm_personid
                and cm_name like '%{}%'
            group by p_pictureid
            limit 50
        """.format(user_input)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: user id
    :return: all movies in the user's watchlist
'''
def get_media_watchlist(user_id):

    conn = open_connection(r'test.sqlite3')

    try:
        sql = """
            select p_pictureid, p_name, mwl_watchstatus, mwl_completitiondate
            from picture, media_watchlist
            where p_pictureid = mwl_pictureid
                and mwl_userid = {}
            order by mwl_id desc
        """.format(user_id)

        cur = conn.cursor()

        cur.execute(sql)

        return cur.fetchall()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')

'''
    :param1: user id
    :param2: picture id
    :return: adds picture to watchlist table
'''
def add_to_watchlist(user_id, picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        print('trying to add to media watchlist')

        sql = """
            insert into Media_Watchlist
            values(null, {}, '{}', 'Recently Added', 'NA')
        """.format(user_id, picture_id)
        
        print(sql)


        conn.execute(sql)

        conn.commit()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')


'''
    :param1: user id
    :param2: picture id
    :return: removes picture from watchlist
'''
def remove_from_watchlist(user_id, picture_id):

    conn = open_connection(r'test.sqlite3')

    try:
        print('trying to add to media watchlist')

        sql = """
            delete from Media_Watchlist
            where mwl_userid = {}
                and mwl_pictureid = '{}'
        """.format(user_id, picture_id)
        
        print(sql)


        conn.execute(sql)

        conn.commit()

    except Error as e:
        print(e)

        # more info about error
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

        conn.rollback()

    close_connection(conn, r'test.sqlite3')