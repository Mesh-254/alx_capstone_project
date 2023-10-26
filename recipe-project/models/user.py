#!/usr/bin/python3
from datetime import datetime
from hashlib import md5
from .database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """user model for the project"""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(300), nullable=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)

    def get_id(self):
        # This method returns a string representation of the user's ID
        return str(self.user_id)

    def avatar(self, size):
        # This method generates a Gravatar URL for the user's avatar based on their email and the desired size
        # 1. Calculate an MD5 hash of the user's lowercase email
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()

        # 2. Construct a Gravatar URL using the hash and the desired size
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    # Initialize the User model with name, email, and password

    def __init__(self, name, email, password):
        self.name = name
        # Note: This should likely be self.password_hash to match the set_password method.
        self.password = password
        self.email = email

    # Method to represent the User object as a string
    def __repr__(self):
        #return a dictionary representation of the User instance.
        return vars(User)
