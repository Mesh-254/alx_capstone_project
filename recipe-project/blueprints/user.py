#!/usr/bin/python3
"""Module to display User information """
from datetime import datetime
from hashlib import scrypt
import re
from flask import *
import pytz
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash


from models.user import User
from models.database import db


user = Blueprint('user', __name__)


@user.route('/user/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first_or_404()
    user_info = [
        {"Name": user.name},
        {"Email": user.email},
    ]
    return render_template('user/profile.html', user=user, user_info=user_info)


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


@user.route('/change-password')
@login_required
def change_password():
    """Change Password method"""
    user = User.query.filter(
            User.user_id == current_user.user_id).first_or_404()
    if request.method == 'POST':
        oldpassword = request.form.get('oldpassword')
        password = request.form.get('newpassword')
        confirm_password = request.form.get('newpassword1')
        user = User.query.filter(
            User.user_id == current_user.user_id).first_or_404()

        if oldpassword == password:
            print('New password should be different from previous password', 'danger')
            return redirect(url_for('profile.change_password'))
        if password != confirm_password:
            print("Passwords do not match")
            return redirect(url_for('profile.change_password'))

        # Check if the password length is at least 8 characters
        if len(password) < 8 or len(confirm_password) < 8:
            flash("Password must be at least 8 characters long.")
            return redirect(url_for('profile.change_password'))

        # Check if the password contains at least one lowercase and one uppercase letter
        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            flash("Password must contain both uppercase and lowercase characters.")
            return redirect(url_for('profile.change_password'))

        # Check if the password contains at least one digit
        if not re.search(r'\d', password):
            flash("Password must contain at least one digit.")
            return redirect(url_for('profile.change_password'))

        # Check if the password contains at least one special character
        if not re.search(r'[!@#$%^&*()_+{}[\]:;<>,.?~\\-]', password):
            flash("Password must contain at least one special character.")
            return redirect(url_for('profile.change_password'))
        if scrypt.hash(user.password, oldpassword):
            user.password = generate_password_hash(password, method='scrypt')
            db.session.commit()
            print('Password changed successfully.', 'success')
            return redirect(url_for('auth.logout'))
        else:
            print('wrong password', 'danger')
            return redirect(url_for('profile.change_password'))
    return render_template('user/change_password.html', user=user)
