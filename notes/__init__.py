from flask import Flask

from . import db
from .controllers import register_blueprints

# init app and configuration
app = Flask(__name__)

# init services
db.init_app(app)

# register controllers/blueprints
register_blueprints(app)
