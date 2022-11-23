from flask import Flask, redirect, url_for, request, abort, render_template, flash, make_response, jsonify

# load database and query functions
from queries import *

app = Flask(__name__)

# Render login page
@app.route('/')
def login_page():
    return render_template('login.html')
    
# Handle login request
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user = get_user_info(request.json['u_username'], request.json['u_password'])

        if(user == None):
            flash('Invalid credentials')
        else:
            print('redirecting')
            return {"redirect": url_for('user_dashboard')}

    return {"redirect": url_for('login_page')}


# Render user dashboard
@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():
    return render_template('user_dashboard.html')

# Render non-user dashboard
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html')

# Filter results by method
@app.route('/search_by/<string:method>', methods=['GET', 'POST'])
def search_by(method):

    if(method == 'no_filter'):

        query = search_by_no_filter() # method defined in queries.py

        data = jsonify({'pictures': query}) # package query into a json format
        response = make_response(data, 200)
        return response

    elif(method == 'streaming_platform'):
        print(request.json['user_input'])
        return 

    return make_response(200)

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