from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from wtforms.validators import Required, Email, Length,     EqualTo
from wtforms import ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remenber me')
    submit = SubmitField('Sign In')
    