#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

# set up of the static folder correctly to serve static files.
app.static_folder = 'static'

app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display landing page"""
    return render_template('/main/index.html')


@app.route('/base')
def base():
    """display base page"""
    return render_template('/main/base.html')


@app.route('/login')
def login():
    """display login page"""
    return render_template('/user/login.html')

@app.route('/signup')
def signup():
    """display login page"""
    return render_template('/user/signup.html')

@app.route('/detail')
def recipe_detail():
    """display login page"""
    return render_template('/main/recipe-detail.html')




if __name__ == '__main__':
    app.run(debug=True)
