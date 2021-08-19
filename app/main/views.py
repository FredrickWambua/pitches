import re
from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required
from . import main
from ..models import User, Pitch, Comment
from .forms import updateProfile
from .. import db

@main.route('/pitch/', methods =['GET', 'POST'])
@login_required
def new_pitch(id):


    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user =  user)
