from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), unique = True)
    passcode = db.Column(db.String(250))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.passcode = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.passcode, password)
    
    def __repr__(self):
        return f'User {self.name}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250))
    category = db.Column(db.String(250))
    pitch = db.Column(db.String(300))
    posted_at = db.Column(db.String(300))
    users = db.relationship('User', backref='pitch', lazy='dynamic')
    
    def __repr__(self):
        return f'Pitch {self.title}, {self.pitch}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(250))
    posted_at = db.Column(db.String(300))

    
    def __repr__(self):
        return f"Comment {self.title}, {self.pitch}"
