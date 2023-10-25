#!/usr/bin/python3
"""Module for user reviews and ratings """
from flask import *
from flask_login import current_user, login_required

from models.user import User
from models.recipe import Recipe
from models.comment import Comment
from models.rating import Rating

from models.database import db

review = Blueprint('review', __name__)

@login_required
@review.route('/add_comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    """Function to add a new comment"""

    # Check if the request method is POST
    if request.method == 'POST':
        # Check if the user is authenticated
        if not current_user.is_authenticated:
            # Return a JSON response with an error message and status code 401 (Unauthorized)
            flash('You are not logged in', 'danger')
            return redirect(url_for('auth.login'))
        
        # Get the comment text from the form data
        comment_text = request.form.get('feedback-user-review')

        # Check if the comment text is provided
        if not comment_text:
            # Return a JSON response with an error message and status code 400 (Bad Request)
            flash('comment text is required', 'success')
            return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

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
        flash('comment submitted successfully', 'success')
        return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

    flash('Error in form', 'danger')
    return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

@login_required
@review.route('/submit-rating/<int:recipe_id>', methods=['POST'])
def submit_rating(recipe_id):
    """Function to add or update a rating for a recipe"""
    if request.method == 'POST':
        if not current_user.is_authenticated:
            # Redirect to the login page
            flash('You are not logged in', 'danger')
            return redirect(url_for('auth.login'))

        # Get the rating value from the request and convert it to an integer
        rating = int(request.form.get('rating'))
        if rating < 1 or rating > 5:
            flash('Invalid rating value', 'danger')
            return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

        # Check if the user has already rated this recipe
        existing_rating = Rating.query.filter_by(
            user_id=current_user.user_id, recipe_id=recipe_id).first()
        if existing_rating:
            flash('You have already registered a rating for this recipe', 'warning')
        else:
            # Create a new Rating object and save it to the database
            new_rating = Rating(
                user_id=current_user.user_id,
                recipe_id=recipe_id,
                rating=rating
            )

            db.session.add(new_rating)
            db.session.commit()

            flash('Rating submitted successfully', 'success')
        return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

    flash('Error in form', 'danger')
    return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))
