#!/usr/bin/python3

"""Module to fetch user information"""

# Import necessary modules
from flask import *
import re  # Import the regular expression module
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user

# Import user-related models and database
from models.user import User
from models.database import db

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Route for displaying the login form


@auth.route('/login')
def login():
    """Display the login form."""
    # Render the login form if it's a GET request
    return render_template('user/login.html')

# Route for handling login requests (GET and POST)


@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    """Handle user login."""
    # Fetch data from the form
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # Check if the user already exists
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('You are not registered. Please signup now.', category="danger")
        # Redirect to the signup page if the user doesn't exist
        return redirect(url_for('auth.signup'))

    if not check_password_hash(user.password, password):
        flash('Please check your login details and try again.', category='danger')
        # Redirect to the login page if the password is incorrect
        return redirect(url_for('auth.login'))
    else:
        login_user(user, remember=remember)  # Log in the user
        flash('You have successfully logged in', 'success')
        # Redirect to the main page after successful login
        return redirect(url_for('recipes.index'))

# Route for displaying the signup form and handling signup requests


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Display the signup form and handle user registration."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Password validations

        # Check if the entered password matches the confirmation password
        if password != confirm_password:
            flash("Passwords do not match", 'danger')
            return redirect(url_for('auth.signup'))

        # Check if the password length is at least 8 characters
        if len(password) < 8 or len(confirm_password) < 8:
            flash("Password must be at least 8 characters long.", 'danger')
            return redirect(url_for('auth.signup'))

        # Check if the password contains at least one lowercase and one uppercase letter
        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            flash(
                "Password must contain both uppercase and lowercase characters.", 'danger')
            return redirect(url_for('auth.signup'))

        # Check if the password contains at least one digit
        if not re.search(r'\d', password):
            flash("Password must contain at least one digit.", 'danger')
            return redirect(url_for('auth.signup'))

        # Check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
            flash("Password must contain at least one special character.", 'danger')
            return redirect(url_for('auth.signup'))

        # Email validation

        # Check if the entered email is in a valid format using a regular expression
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #     flash("Invalid email address.")
        #     return redirect(url_for('auth.signup'))

        # Check if the email is already in use
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email address already taken.", 'danger')
            return redirect(url_for('auth.signup'))

        # Create a new user and add them to the database
        new_user = User(name=name, email=email, password=generate_password_hash(
            password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully! You can log in below.", 'success')
        return redirect(url_for('auth.login'))

    # Render the signup form if it's a GET request
    return render_template('user/signup.html')

# Route for logging out the user


@auth.route('/logout')
def logout():
    """Logout the user and redirect to the main page."""
    logout_user()
    return redirect(url_for('recipes.index'))
