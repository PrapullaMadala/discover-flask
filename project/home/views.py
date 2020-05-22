###############
### imports ###
###############

from project import db
from project.models import BlogPost
from flask import render_template, request, redirect, url_for, session, flash, Blueprint
from project.users.forms import LoginForm
from functools import wraps


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


########################
### helper functions ###
########################

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('home.login'))
    return wrap


##############
### routes ###
##############
# use decorators to link the functions to a url

@home_blueprint.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
       
    return render_template("index.html", posts=posts) # render a template

@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html") # render a template

@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
            error = "Invalid credentials. Please try again."
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home.home'))                
    return render_template('login.html', error = error, form = form)

@home_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home.welcome'))
