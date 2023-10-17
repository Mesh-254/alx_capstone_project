from models.database import db
from flask_login import UserMixin


class Recipes(db.Model, UserMixin):
    """recipes model for the project"""
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    rating = db.Column(db.integer)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    user = db.relationship('Users', backref='recipes')

    def __repr__(self):
        return vars(Recipes)
