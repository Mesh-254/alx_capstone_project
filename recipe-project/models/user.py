#!/usr/bin/python3
from .database import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    """user model for the project"""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(300), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)

    def get_id(self):
        return str(self.user_id) 

    # Initialize the User model with name, email, and password

    def __init__(self, name, email, password):
        self.name = name
        # Note: This should likely be self.password_hash to match the set_password method.
        self.password = password
        self.email = email

    # Method to represent the User object as a string
    def __repr__(self):
        # It should likely be return str(vars(self)) to return a dictionary representation of the User instance.
        return vars(User)
