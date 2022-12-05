from flask import Flask, redirect, url_for, request, abort, render_template, flash, make_response, jsonify

# load database and query functions
from queries import *

app = Flask(__name__)
app.secret_key = "super secret key"

# Render login page
@app.route('/')
def login_page():
    return render_template('login.html')
    
# Handle login request
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        global user
        user = get_user_info(request.json['u_username'], request.json['u_password'])

        if(user == None):
            flash('Invalid credentials')
        else:
            print('redirecting')
            return {"redirect": url_for('user_dashboard')}

    return {"redirect": url_for('login_page')}





# Render registration page
@app.route('/register')
def register_page():
    #print("nice2")
    return render_template('register.html')

# Handle registration request
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        global newuser
        #print("finish")    
        #flash(request.json['u_username'])
        newuser = register_user(request.json['u_username'], request.json['u_password'], request.json['u_email'], request.json['u_firstname'], request.json['u_lastname'], request.json['u_preferredstreamsite'])

        
        if(newuser == None):
            flash('Invalid credentials')
        else:
            #print('redirecting')
            #return {"redirect": url_for('')} #log in again
            return {"redirect": url_for('login_page')}

    return {"redirect": url_for('register_page')}







# Render user dashboard
@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():
    print(user)
    name = user[4] + ' ' + user[5]

    watchlist = get_media_watchlist(user[0])
    print(watchlist)

    return render_template('user_dashboard.html', name=name, watchlist=watchlist)

# Render non-user dashboard
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html')

# Filter results by method
@app.route('/search_by/<string:method>', methods=['GET', 'POST'])
def search_by(method):
    user_input = [request.json['user_input']]
    user_input += request.json['user_input'].split(' ')
    

    print(user_input)

    if method == 'no_filter':

        query = search_by_no_filter() # method defined in queries.py

        data = jsonify({'pictures': query}) # package query into a json format
        response = make_response(data, 200)
        return response

    elif method == 'release_year':
        user_input = request.json['user_input'].split(' ')

        query = []
        
        for item in user_input:
            query += search_by_release_year(item)
        
        data = jsonify({'pictures': query})
        response = make_response(data, 200)
        return response

    elif method == 'picture_name':
        query = []

        for item in user_input:
            query += search_by_picture_name(item)
             
        data = jsonify({'pictures': query})
        response = make_response(data, 200)
        return response

    elif method == 'cast_member_name':
        
        query = []

        for item in user_input:
            query += search_by_cast_member_name(item)
             
        data = jsonify({'pictures': query})
        response = make_response(data, 200)
        return response


    return make_response()

# Load additional information about movie
@app.route('/more_info_picture/<string:picture_id>', methods=['GET'])
def search_by_picture(picture_id):
    data = get_picture_info(picture_id)

    title = data[1]
    release_year = data[2]
    age_rating = data[3]
    genres = data[4].split(", ")

    streaming_sites = get_streaming_availability(picture_id)
    
    ratings = get_public_ratings(picture_id)

    #default values
    RTrating = ''
    IMDbrating = ''

    if len(ratings)  == 2:
        RTrating = ratings[0]
        IMDbrating = ratings[1]

    user_reviews = get_user_reviews(picture_id)

    cast_members = get_media_cast_members(picture_id)

    return render_template('picture.html',  \
        title=title, release_year=release_year, age_rating=age_rating, genres=genres, \
        streaming_sites=streaming_sites, RTrating=RTrating, IMDbrating=IMDbrating,    \
        user_reviews=user_reviews, cast_members=cast_members)

if __name__ == '__main__':
    app.run(debug=True)
