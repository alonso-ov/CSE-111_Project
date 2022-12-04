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
        global user
        user = get_user_info(request.json['u_username'], request.json['u_password'])

        #check if user is an admin
        if isAdmin(user[0])[0][0] == 1:
            return  {"redirect": url_for('admin_dashboard')}

        if(user == None):
            flash('Invalid credentials')
        else:
            print('redirecting')
            return {"redirect": url_for('user_dashboard')}

    return {"redirect": url_for('login_page')}

@app.route('/admin_dashboard', methods=["GET", "POST"])
def admin_dashboard():
    name = user[4] + ' ' + user[5]
    return render_template("admin.html", name=name)


# Render user dashboard
@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():
    #print(user)
    name = user[4] + ' ' + user[5]

    watchlist = get_media_watchlist(user[0]);

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

    notInWatchlist = False
    hasLoggedIn = False

    # check if user variable exists
    if 'user' in globals() and user != None:
        hasLoggedIn = True

        watchlist = get_media_watchlist(user[0])

        watchlist_pictures_id = [i[0] for i in watchlist]

        if not picture_id in watchlist_pictures_id:
            notInWatchlist = True
        

    return render_template('picture.html',  \
        title=title, release_year=release_year, age_rating=age_rating, genres=genres,       \
        streaming_sites=streaming_sites, RTrating=RTrating, IMDbrating=IMDbrating,          \
        user_reviews=user_reviews, cast_members=cast_members, notInWatchlist=notInWatchlist, \
        picture_id=picture_id, hasLoggedIn=hasLoggedIn)

# Load additional information about movie
@app.route('/addToWatchlist/<string:picture_id>', methods=['PUT'])
def addToWatchlist(picture_id):
    
    # check if user is initialized
    if 'user' in globals():
        #check if user has picture already
        watchlist = get_media_watchlist(user[0]);

        watchlist_pictures_id = [i[0] for i in watchlist]

        if not picture_id in watchlist_pictures_id:
            #add picture to watchlist
            add_to_watchlist(user[0], picture_id)
            return make_response('successfully added to watchlist', 201)

    return make_response('user does not exist', 400)

@app.route('/removeFromWatchlist/<string:picture_id>', methods=['DELETE'])
def removeFromWatchlist(picture_id):
    if 'user' in globals():
        remove_from_watchlist(user[0], picture_id)

        return make_response('delete picture from user watchlist', 200)

@app.route('/editWatchlist/<string:picture_id>', methods=['PUT'])
def editWatchlist(picture_id):
    watchstatus = request.json['watchstatus']
    completitiondate = request.json['completitiondate']

    if 'user' in globals():
        update_watchlist(user[0], picture_id, watchstatus, completitiondate)

    return make_response('Could not process request', 400)

@app.route('/logout', methods=["POST"])
def logout():
    global user
    user = None

    return {"redirect": url_for('login_page')}

@app.route('/addComment/<string:picture_id>', methods=["POST"])
def addComment(picture_id):
    print(picture_id)
    
    if 'user' in globals():
        add_comment(picture_id, user[0], request.form['comment'], request.form['rating'])

        return redirect(url_for('search_by_picture', picture_id=picture_id))

    return make_response()

@app.route('/addMovie', methods=['POST'])
def addMovie():
    print(request.form)
    return make_response()

if __name__ == '__main__':
    app.run(debug=True)