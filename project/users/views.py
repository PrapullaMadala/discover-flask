#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint, session  # pragma: no cover
from functools import wraps
from app import app
from flask_bcrypt import Bcrypt
from .forms import LoginForm  # pragma: no cover

################
#### config ####
################
bcrypt = Bcrypt(app)

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)   # pragma: no cover

# login required decorator
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for(users.login))
    return wrap

################
#### routes ####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])   # pragma: no cover
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
            error = "Invalid credentials. Please try again."
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))                
    return render_template('login.html', error = error, form = form)


@users_blueprint.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))
