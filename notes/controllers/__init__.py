from flask import jsonify, Flask

from .home import home_blueprint
from .notes import notes_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(notes_blueprint, url_prefix="/notes")
