from flask import Flask

from .db import db, migrate
from .controllers import register_blueprints

# init app and configuration
app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init services
db.init_app(app)
migrate.init_app(app, db)

# register controllers/blueprints
register_blueprints(app)
