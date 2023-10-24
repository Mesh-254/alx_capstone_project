from .database import db
from flask_login import UserMixin


class Recipe(db.Model, UserMixin):
    """recipes model for the project"""
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    source_url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='recipe', lazy=True)
    ratings = db.relationship('Rating', backref='recipe', lazy=True)

    def __repr__(self):
        return vars(Recipe)
