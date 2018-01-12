from flask import Flask

# Initialize the app
# if we set instante_relative_config to True we can use app.config.from_object('config') to load the config.py file
app = Flask(__name__, instance_relative_config=True)

# load the views
from app import views

# load the config file
app.config.from_object('config')
