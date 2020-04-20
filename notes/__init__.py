from flask import Flask

from .controllers import register_blueprints

app = Flask(__name__)

register_blueprints(app)
