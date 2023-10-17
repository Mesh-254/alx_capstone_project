from flask import *
from flask_migrate import Migrate
from flask.cli import load_dotenv
import os


# flask login
# from flask_login import LoginManager

# import models tables
from models.database import db
# from models.user import User
# from models.recipes import Recipes
# from models.comments import Comments

# import of blueprints 
from blueprints.recipes import recipes

# application
app = Flask(__name__, template_folder='./templates')

app.url_map.strict_slashes = False


# set up of the static folder correctly to serve static files.
app.static_folder = 'static'


# load environment variables
env = load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"


db.app = app
db.init_app(app)
migrate = Migrate(app, db)

# register blueprints
app.register_blueprint(recipes,url_prefix='/')


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'auth.login'


# @app.route('/')
# def index():
#     """display landing page"""
#     return render_template('/main/index.html')


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
    app.run(debug=True, host="0.0.0.0", port=5000)
