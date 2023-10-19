#!/usr/bin/python3
from .database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    """user model for the project"""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy=True)
    ratings = db.relationship('Rating', backref='user', lazy=True)

    # Method to hash the user's password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to check if the provided password matches the hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
