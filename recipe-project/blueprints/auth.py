#!/usr/bin/python3
"""Module to fetch user information """
from flask import *

auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    """function to perform login"""
    return render_template('/user/login.html')


@auth.route('/signup')
def signup():
    """Function to perform signup of users"""
    return render_template('/user/signup.html')


