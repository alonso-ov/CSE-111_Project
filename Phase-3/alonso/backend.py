import sqlite3
from sqlite3 import Error
from flask import Flask, redirect, url_for, request, abort, render_template, flash, make_response
from handle_db import *
from queries import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'place secret key here'

@app.route('/')
def login_page():
    return render_template('login.html')
    
# Login requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user = get_user(request.json['u_username'], request.json['u_password'])

        if(user == None):
            flash('Invalid credentials')
        else:
            print('redirecting')
            return {"redirect": url_for('user_dashboard')}

    return {"redirect": url_for('login_page')}


@app.route('/user_dashboard', methods=['GET', 'POST'])
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html')

@app.route('/search_by/<string:method>', methods=['GET'])
def no_filter(method):
    if(method == 'no_filter'):
        query = search_by_no_filter()
        print(query)

if __name__ == '__main__':
    app.run(debug=True)