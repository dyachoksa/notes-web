from flask import Blueprint, render_template, request, redirect, url_for

from ..db import db
from ..models import Category

categories_blueprint = Blueprint("categories", __name__)


@categories_blueprint.route("", endpoint="index")
def get_list():
    categories = Category.query.all()

    return render_template("categories/index.html", categories=categories)


@categories_blueprint.route("/create", methods=["GET", "POST"])
def create():
    category = Category()

    context = {"category": category}

    if request.method == "POST":
        category.name = request.form["name"]

        if len(category.name) < 3:
            error = "Please check your form. All fields are required."
            context["error"] = error
            return render_template("categories/create.html", **context)

        try:
            db.session.add(category)
            db.session.commit()
        except Exception as err:
            context["error"] = str(err)
            return render_template("categories/create.html", **context)

        return redirect(url_for("categories.index"))

    return render_template("categories/create.html", **context)


@categories_blueprint.route("/<int:category_id>/edit", methods=["GET", "POST"])
def edit(category_id):
    category = Category.query.get_or_404(category_id)

    context = {"category": category}

    if request.method == "POST":
        category.name = request.form["name"]

        if len(category.name) < 3:
            error = "Please check your form. All fields are required."
            context["error"] = error
            return render_template("categories/edit.html", **context)

        try:
            # db.session.add(category)
            db.session.commit()
        except Exception as err:
            context["error"] = str(err)
            return render_template("categories/edit.html", **context)

        return redirect(url_for("categories.index"))

    return render_template("categories/edit.html", **context)
