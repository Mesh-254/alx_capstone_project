#!/usr/bin/python3
"""Module to display User information """
from flask import *
from flask_login import login_required


from models.user import User
from models.database import db


user = Blueprint('user', __name__)

@app.route('/user/<email>')
@login_required
def user(email):
    user = User.query.filter_by(email=email).first_or_404()
    user_info = [
        {'Name': user.name},
        {"Email": user.email}
    ]

    return render_template('')