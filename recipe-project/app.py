# Import necessary modules from Flask and other libraries
from flask import Flask, render_template
from flask_migrate import Migrate
from flask.cli import load_dotenv
import os

# Import Flask-Login for user authentication
from flask_login import LoginManager

# Import database models
from models.database import db
from models.user import User
from models.recipe import Recipe
from models.comment import Comment
from models.rating import Rating

# Import blueprints for routing
from blueprints.recipes import recipes
from blueprints.auth import auth
from blueprints.user import user
from blueprints.reviews import review


from flask_bcrypt import Bcrypt



# Create a Flask application
app = Flask(__name__, template_folder='./templates')

# Configure the application to not force trailing slashes on URLs
app.url_map.strict_slashes = False

# Configure the static folder to serve static files (like CSS, JavaScript, etc.)
app.static_folder = 'static'

# Load environment variables from a .env file
env = load_dotenv()
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')

# Configure the Flask application with various settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"


# Initialize the database and set up migration support
db.init_app(app)
migrate = Migrate(app, db)


# Register blueprints to organize routes
app.register_blueprint(recipes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(user, url_prefix='/')
app.register_blueprint(review, url_prefix='/')

# Create a LoginManager instance and configure it
login = LoginManager()
login.init_app(app)
login.login_view = 'auth.login'

bcrypt = Bcrypt(app)

# Function decorator to load a user by their ID when needed for authentication
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define a route to display a base page


@app.route('/base')
def base():
    """display base page"""
    return render_template('/main/base.html')




# Start the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
