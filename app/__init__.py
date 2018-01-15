from flask import Flask, render_template

# Initialize the app
# if we set instante_relative_config to True we can use app.config.from_object('config') to load the config.py file
app = Flask(__name__)

# load the config file
app.config.from_object('config')

from app.views import home
app.register_blueprint(home.mod)

from app.views import remote
app.register_blueprint(remote.mod)

from app.views import contact
app.register_blueprint(contact.mod)

from app.views import manual
app.register_blueprint(manual.mod)
