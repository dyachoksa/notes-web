from flask import Blueprint, render_template

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
def index():
    app_name = "Notes App"
    app_description = "Notes management application"

    return render_template("index.html", name=app_name, description=app_description)
