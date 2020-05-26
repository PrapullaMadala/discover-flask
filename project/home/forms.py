from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired, Length
import email_validator

class MessageForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired(), Length(max=140)])