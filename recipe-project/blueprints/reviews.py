#!/usr/bin/python3
"""Module for user reviews and ratings """
from flask import *
from flask_login import current_user

from models.user import User
from models.recipe import Recipe
from models.comment import Comment

from models.database import db

review = Blueprint('review', __name__)


@review.route('/add_comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    """Function to add a new comment"""

    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the user is authenticated
        if not current_user.is_authenticated:
            # Return a JSON response with an error message and status code 401 (Unauthorized)
            return jsonify({'error': 'User not authenticated'}), 401

        # Get the comment text from the form data
        comment_text = request.form.get('feedback-user-review')

        # Check if the comment text is provided
        if not comment_text:
            # Return a JSON response with an error message and status code 400 (Bad Request)
            return jsonify({'error': 'Comment text is required'}), 400

        # Create a new Comment object
        comment = Comment(
            user_id=current_user.user_id,  # Associate the comment with the current user
            recipe_id=recipe_id,  # Associate the comment with the specified recipe
            comment_text=comment_text  # Set the comment text
        )

        # Add the comment to the database session
        db.session.add(comment)
        # Commit the changes to the database
        db.session.commit()

        # redirect to view page
        return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))
        
    return jsonify({'error': 'There was an error in form'}), 201
