from .database import db
from flask_login import UserMixin


class Rating(db.Model, UserMixin):
    """Rating model for the project"""
    __tablename__ = 'ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipes.recipe_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
