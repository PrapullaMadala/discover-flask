from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) 