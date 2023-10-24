from .database import db
from flask_login import UserMixin


class Comment(db.Model, UserMixin):
    """comments model for the project"""

    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey(
        'recipes.recipe_id'), nullable=False)
    comment_text = db.Column(db.Text, nullable=True)
    comment_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp())
