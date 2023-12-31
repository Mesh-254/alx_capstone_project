#!/usr/bin/python3
"""Module to display User information"""

# Import necessary modules and libraries
from datetime import datetime
from hashlib import scrypt
import re
from flask import *
import pytz
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Import User model and database from the application
from models.user import User
from models.database import db

# Create a Flask Blueprint named 'user' for this module
user = Blueprint('user', __name__)

# Define a route to display user profile information
@user.route('/user/<email>')
@login_required
def profile(email):
    """Display user profile information"""
    # Query the User model to retrieve user information by email
    user = User.query.filter_by(email=email).first_or_404()
    
    # Create a list with user information
    user_info = [
        {"Name": user.name},
        {"Email": user.email},
    ]

    # Render the 'user/profile.html' template and pass user and user_info as context
    return render_template('user/profile.html', user=user, user_info=user_info)

# Define a function to be executed before each request
@user.before_request
def before_request():
    # This function is executed before each request to the application

    if current_user.is_authenticated:
        # Check if the current user is authenticated

        # Update the 'last_seen' attribute for the authenticated user
        east_african_timezone = pytz.timezone('Africa/Nairobi')
        current_user.last_seen = datetime.now(east_african_timezone)

        # Commit the changes to the database
        db.session.commit()

# Define a route to change the user's password
@user.route('/change-password', methods=['POST', 'GET'])
@login_required
def change_password():
    """Change Password method"""
    user = User.query.filter(
            User.user_id == current_user.user_id).first_or_404()
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        password = request.form.get('newpassword')
        confirm_password = request.form.get('newpassword1')
        
        # Check if the old password matches the user's current password
        if check_password_hash(user.password, oldpassword):
            # Check if the new password is the same as the old password
            if oldpassword == password:
                flash('New password should be different from the previous password', 'danger')
                return redirect(url_for('user.change_password'))
            
            # Check if the new password and the confirmation match
            if password != confirm_password:
                flash("Passwords do not match!", 'danger')
                return redirect(url_for('user.change_password'))

            # Check if the password length is at least 8 characters
            if len(password) < 8 or len(confirm_password) < 8:
                flash("Password must be at least 8 characters long.", 'danger')
                return redirect(url_for('user.change_password'))

            # Check if the password contains at least one lowercase and one uppercase letter
            if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
                flash("Password must contain both uppercase and lowercase characters.", 'danger')
                return redirect(url_for('user.change_password'))

            # Check if the password contains at least one digit
            if not re.search(r'\d', password):
                flash("Password must contain at least one digit.", 'danger')
                return redirect(url_for('user.change_password'))

            # Check if the password contains at least one special character
            if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
                flash("Password must contain at least one special character.", 'danger')
                return redirect(url_for('user.change_password'))

            # Update the user's password with the new password and commit the change to the database
            user.password = generate_password_hash(password, method='sha256')
            db.session.commit()
            flash('Password changed successfully.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Wrong password', 'danger')
            return redirect(url_for('user.change_password'))
    return render_template('user/change_password.html', user=user)

# Define a route to display the user's favorite recipes
@user.route('/favorite-recipes')
@login_required
def favorite_recipes():
    """Function to render favorite recipe page"""
    # Query the User model to retrieve user information by email
    user = User.query.filter_by(email=current_user.email).first_or_404()
    
    # Render the 'user/favorite_recipes.html' template and pass user as context
    return render_template('user/favorite_recipes.html', user=user)

@user.route('/contact')
def contact():
    """function to handle contacts"""
    return render_template('user/contact_page.html')