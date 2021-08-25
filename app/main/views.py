
import re
from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required, current_user
from flask_migrate import current
from flask_wtf import form
from . import main
from ..models import User, Pitch, Comment
from .forms import  UpdateProfile, PitchForm,CommentForm
from .. import db,photos

@main.route('/')
def index():
    pitches = Pitch.query.all()
    product = Pitch.query.filter_by(category = 'Product').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all()
    pick_up_lines = Pitch.query.filter_by(category = 'Pick Up Lines').all()
    interviews = Pitch.query.filter_by(category = 'Interviews').all()

    return render_template('index.html', pitches = pitches, product = product, promotion = promotion, pick_up_lines = pick_up_lines, interviews = interviews)


@main.route('/user/<uname>')
def update_profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)


@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_prof(uname):
    user = User.query.filter_by(name = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

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



@main.route('/add_pitch/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category =form.category.data
        pitch = form.pitch.data
        title = form.title.data
        new_pitch = Pitch(title=title, category=category, pitch=pitch, user_id=current_user._get_current_object().id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('add_pitch.html', form = form)


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comment()

        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)
