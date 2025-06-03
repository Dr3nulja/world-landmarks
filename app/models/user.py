from datetime import datetime
from app.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 

    landmarks = db.relationship('Landmark', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)
    photos = db.relationship('Photo', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
