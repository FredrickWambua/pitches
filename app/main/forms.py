from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms import validators
from wtforms.validators import Required, Email
from ..models import User, Pitch, Comment

class updateProfile(FlaskForm):
    bio = TextAreaField('Say more about you.', validators = [Required()])
    submit = SubmitField('Submit')