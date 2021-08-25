from flask.globals import request
from flask.helpers import flash
from flask_login.utils import login_required, login_user, logout_user
from app.email import mail_message
from flask import render_template,redirect,url_for
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. email import mail_message
from .. import db
from . import auth


# login view function
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
           login_user(user,form.remember.data) 
           return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
        title = 'Login'
    return render_template('auth/login.html', login_form = form)

# registration view function

@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, name = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message('Welcome to The Pitch', 'email/welcome_user', user.email, user=user)
        
        title = 'New account'

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registration_form = form)


# logout view function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
