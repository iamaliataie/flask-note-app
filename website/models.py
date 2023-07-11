from datetime import datetime
from . import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
