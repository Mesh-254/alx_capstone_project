from models.database import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    """user model for the project"""
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(300), unique=True, nullable=False)

    def __init__(self, name, email, password):
        """Initialize the user model"""
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return vars(Users)
