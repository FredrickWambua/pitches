from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import main

@main.route('/pitch/', methods =['GET', 'POST'])
@login_required
def new_pitch(id):


    return render_template('index.html')
