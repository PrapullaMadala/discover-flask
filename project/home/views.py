###############
### imports ###
###############

from project import db # pragma: no cover
from project.models import BlogPost # pragma: no cover
from flask import render_template, request, redirect, url_for, session, flash, Blueprint # pragma: no cover
from project.users.forms import LoginForm # pragma: no cover
from flask_login import login_required, current_user# pragma: no cover
from functools import wraps # pragma: no cover
from .forms import MessageForm # pragma: no cover


################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


##############
### routes ###
##############
# use decorators to link the functions to a url

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])   # pragma: no cover
@login_required   # pragma: no cover
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        posts = db.session.query(BlogPost).all()
        return render_template(
            'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template("welcome.html") # render a template
