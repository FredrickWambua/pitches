import re
from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required
from flask_wtf import form
from . import main
from ..models import User, Pitch, Comment
from .forms import updateProfile
from .. import db,photos

@main.route('/pitch/', methods =['GET', 'POST'])
@login_required
def new_pitch(id):


    return render_template('index.html')

@main.route('/user/<uname>')
def update_profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    form = updateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.name))

    return render_template('profile/profile.html', form = form)
    
@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile', uname = uname))