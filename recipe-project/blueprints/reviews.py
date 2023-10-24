#!/usr/bin/python3
"""Module for user reviews and ratings """
from flask import *
from flask_login import current_user

from models.user import User
from models.recipe import Recipe
from models.comment import Comment

from models.database import db

review = Blueprint('review', __name__)


@review.route('/comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    """Function to get reviews"""
    if request.method == 'POST':
        # Check if the user is authenticated and get the current user
        if not current_user.is_authenticated:
            return jsonify({'error': 'User not authenticated'}), 401

        # Fetch the recipe from your database using the recipe_id
        recipe = Recipe.query.get(recipe_id)

        if not recipe:
            return jsonify({'error': 'Recipe not found'}), 404

        comment = request.form.get('feedback-user-review')
        print(comment)

        # Create a new Comment object and associate it with the user and recipe
        comment = Comment(
            user_id=current_user.id,
            recipe_id=recipe.id,
            comment_text=comment
        )

        # Add the comment to the database
        db.session.add(comment)
        db.session.commit()

        return jsonify({'message': 'Comment added successfully'}), 200
