#!/usr/bin/python3
"""Module to display User information """
from datetime import datetime
from flask import *
import pytz
from flask_login import login_required, current_user


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
