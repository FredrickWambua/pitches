from flask_wtf import FlaskForm
from flask_wtf.recaptcha.validators import RECAPTCHA_ERROR_CODES
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms import validators, TextAreaField, StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import Required, Email
from ..models import User, Pitch, Comment

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say more about you.', validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Category', choices=[('Product', 'Product'),('Promotion','Promotion'),('Pick Up Lines', 'Pick Up Lines'),('Interviews','Interviews')], validators=[Required()])
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment= TextAreaField('Leave a comment', validators=[Required()])
    submit = SubmitField('Comment')