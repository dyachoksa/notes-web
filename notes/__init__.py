from flask import Flask

from . import db
from .controllers import register_blueprints

# inita app and configuration
app = Flask(__name__)

# init services
db.init_app(app)

# register controllers/blueprints
register_blueprints(app)
