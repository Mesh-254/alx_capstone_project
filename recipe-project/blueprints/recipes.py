#!/usr/bin/python3
"""module to fetch recipe information"""
from flask import *

from flask.cli import load_dotenv
import os
import requests
from urllib.parse import unquote

recipes = Blueprint('recipes', __name__)


env = load_dotenv()

API_KEY = os.getenv('API_KEY')


# render home route
@recipes.route('/home', methods=['GET'])
def home():
    # Render the main page with empty recipe list and search query
    return render_template('/main/index.html', recipes=[], search_query='')

# route to allow users serach for recipes


@recipes.route('/search', methods=['GET', 'POST'])
def search():
    """Function to allow user search for recipes"""
    if request.method == "POST":
        # If a form is submitted
        query = request.form.get('search_query', '')

        # Perform a search for recipes with the given query
        recipes = search_recipes(query)

        # Render the main page with the search results and the search query
        return render_template('main/search_recipe.html', recipes=recipes, search_query=query)
    else:
        # If no form is submitted (user just loaded the page), show an empty result set
        search_query = request.args.get('search_query', '')
        decoded_search_query = unquote(search_query)
        # Perform a search for recipes with the decoded search query
        recipes = search_recipes(decoded_search_query)
        # Render the main page
        return render_template('main/search_recipe.html', recipes=recipes, search_query=decoded_search_query)


# Define the main route for the app
@recipes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If a form is submitted
        query = request.form.get('search_query', '')
        # Perform a search for recipes with the given query
        recipes = search_recipes(query)
        # Render the main page with the search results and the search query
        return render_template('main/index.html', recipes=recipes, search_query=query)

    # If it's a GET request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    # Perform a search for recipes with the decoded search query
    recipes = search_recipes(decoded_search_query)
    # Render the main page
    return render_template('main/index.html', recipes=recipes, search_query=decoded_search_query)

# Function to search for recipes based on the provided query


def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    # Send a GET request to the Spoonacular API with the query parameters
    response = requests.get(url, params=params)
    # If the API call is successful
    if response.status_code == 200:
        # Parse the API response as JSON data
        data = response.json()
        # Return the list of recipe results
        return data['results']
    # If the API call is not successful
    return []


# Route to view a specific recipe with a given recipe ID
@recipes.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    """function to fetch particular recipe details"""
    # Get the search query from the URL query parameters
    search_query = request.args.get('search_query', '')
    # Build the URL to get information about the specific recipe ID from Spoonacular API
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }

    # Send a GET request to the Spoonacular API to get the recipe information
    response = requests.get(url, params=params)
    # If the API call is successful
    if response.status_code == 200:
        recipe = response.json()
        return render_template('main/recipe-detail.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404


# function to show recipes for dish-types
@recipes.route('/recipe-dish-types')
def recipe_dish_types():
    """function to show different dish-types recipes"""
    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Combine dish types with a comma
    DISH_TYPES = 'Cake, Bread, Candy,Fudge,Casserole'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'dish',
        'number': 20,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for particular type
@recipes.route('/recipe-meal-types')
def recipe_meal_types():
    """function to show different meal-types recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'
    # Combine MEAL types with a comma
    MEAL_TYPES = 'Breakfast, Brunch, Desserts, Dinners, Lunch'
    for meal in MEAL_TYPES:

        # Make a request to the Spoonacular API for each list name
        params = {
            'apiKey': API_KEY,
            'query': meal,
            'number': 5,  # You can adjust the number of recipes to retrieve
            'instructionsRequired': True,
            'addRecipeInformation': True,
            'fillIngredients': True,
        }
        response = requests.get(BASE_URL, params=params)
        if (response.status_code == 200):
            data = response.json()
            recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for particular type
@recipes.route('/recipe-diet-health')
def recipe_diet_health():
    """function to show diet&health recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Diet',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
        return render_template('main/recipes.html', recipes=recipes)
    return "Recipe not found", 404

# function to show recipes for particular type


@recipes.route('/recipe-cuisine')
def recipe_cuisine():
    """function to show cuisine recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'cuisine',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for particular type
@recipes.route('/recipe-seasonal')
def recipe_seasonal():
    """function to show seasonal recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'cuisine',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)

# Different routes to display different queries from categories


# function to show Appetizers recipes
@recipes.route('/recipe-Appetizers')
def recipe_Appetizers():
    """function to display Appetizers recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Appetizers',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Bread Recipes
@recipes.route('/recipe-bread')
def recipe_bread():
    """function to show bread recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'bread',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for cake Recipes
@recipes.route('/recipe-cake')
def recipe_cake():
    """function to show cake recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'bread',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']

    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for candy Recipes
@recipes.route('/recipe-candy')
def recipe_candy():
    """function to show Candy recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'candy',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for casserole Recipes
@recipes.route('/recipe-casserole')
def recipe_casserole():
    """function to show casserole recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'casserole',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Breakfast Recipes
@recipes.route('/recipe-breakfast')
def recipe_breakfast():
    """function to show breakfast recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'breakfast',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for desserts Recipes
@recipes.route('/recipe-desserts')
def recipe_desserts():
    """function to show desserts recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'desserts',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Dinners Recipes
@recipes.route('/recipe-dinners')
def recipe_dinners():
    """function to show dinners recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'dinners',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for lunch Recipes
@recipes.route('/recipe-lunch')
def recipe_lunch():
    """function to show lunch recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'lunch',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)

# function to show recipes for Diabetic Recipes


@recipes.route('/recipe-diabetic')
def recipe_diabetic():
    """function to show Diabetic recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Diabetic',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)

# function to show recipes for Gluten Free Recipes


@recipes.route('/recipe-Gluten-free')
def recipe_gluten_free():
    """function to show Gluten Free recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'glutenfree',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for High Fiber Recipes
@recipes.route('/recipe-high-fiber')
def recipe_high_fiber():
    """function to show High Fiber recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Highfiber',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Low Calorie Recipes
@recipes.route('/recipe-low-calorie')
def recipe_low_calorie():
    """function to show Low Calorie recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'lowcalorie',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for chinese Recipes
@recipes.route('/recipe-chinese')
def recipe_chinese():
    """function to show chinese recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Chinese',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Indian Recipes
@recipes.route('/recipe-indian')
def recipe_indian():
    """function to show indian recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'indian',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for italian Recipes
@recipes.route('/recipe-italian')
def recipe_italian():
    """function to show italian recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'italian',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Mexican Recipes
@recipes.route('/recipe-mexican')
def recipe_mexican():
    """function to show Mexican recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'mexican',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Baby Shower Recipes
@recipes.route('/recipe-baby-shower')
def recipe_baby_shower():
    """function to show Baby Shower recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'babyshower',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Birthday Recipes
@recipes.route('/recipe-birthday')
def recipe_birthday():
    """function to show Birthday recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'birthday',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Christmas Recipes
@recipes.route('/recipe-Christmas')
def recipe_christmas():
    """function to show Christmas recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Christmas',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)


# function to show recipes for Halloween Recipes
@recipes.route('/recipe-halloween')
def recipe_halloween():
    """function to show Halloween recipes"""

    recipes = []
    BASE_URL = 'https://api.spoonacular.com/recipes/complexSearch'

    # Make a request to the Spoonacular API for each list name
    params = {
        'apiKey': API_KEY,
        'query': 'Halloween',
        'number': 5,  # You can adjust the number of recipes to retrieve
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }
    response = requests.get(BASE_URL, params=params)
    if (response.status_code == 200):
        data = response.json()
        recipes += data['results']
    return render_template('main/recipes.html', recipes=recipes)
