# imports
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from forms import LoginForm
from functools import wraps
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


# config
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# create sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the functions to a url
@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
       
    return render_template("index.html", posts=posts) # render a template

@app.route('/welcome')
def welcome():
    return render_template("welcome.html") # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
            error = "Invalid credentials. Please try again."
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))                
    return render_template('login.html', error = error, form = form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))


# start the server with the 'run()' method  
if __name__ == '__main__':
    app.run() 