from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(250), unique = True)
    pitches_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comments = db.relationship('Comment', backref='name', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250))
    category = db.Column(db.String(250))
    pitch = db.Column(db.String(300))
    users = db.relationship('User', backref='pitch')
    
    def __repr__(self):
        return f'Pitch {self.title}, {self.pitch}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(250))
    posted_at = db.Column(db.String(300))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    
    def __repr__(self):
        return f'Pitch {self.title}, {self.pitch}'
