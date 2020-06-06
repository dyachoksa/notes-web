import typing

from flask import Blueprint, render_template, abort, request, redirect, url_for

from ..db import db
from ..models import Note, Category


notes_blueprint = Blueprint("notes", __name__)


def format_notes(notes: typing.List[Note]):
    return [dict(id=note.id, title=note.title, content=note.content) for note in notes]


@notes_blueprint.route("/", endpoint="index")
def get_list():
    notes = Note.query.all()

    return render_template("notes/index.html", notes=notes)


@notes_blueprint.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if len(title) < 3 or len(content) < 3:
            error = "Please check your form. All fields are required."
            return render_template("notes/create.html", error=error, title=title, content=content)

        note = Note(
            title=title,
            content=content,
            category_id=request.form.get("category_id", None)
        )

        db.session.add(note)
        db.session.commit()

        return redirect(url_for("notes.show", note_id=note.id))

    categories = Category.query.all()
    return render_template("notes/create.html", categories=categories, title="", content="")


@notes_blueprint.route("/<int:note_id>", endpoint="show")
def get_one(note_id):
    note = Note.query.get_or_404(note_id)

    return render_template("notes/show.html", note=note)


@notes_blueprint.route("/<int:note_id>/edit", methods=["GET", "POST"])
def edit(note_id):
    note = Note.query.get_or_404(note_id)
    categories = Category.query.all()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        note.category_id = request.form.get("category_id")

        if len(title) < 3 or len(content) < 3:
            error = "Please check your form. All fields are required."

            note.title = title
            note.content = content

            return render_template("notes/edit.html", categories=categories, error=error, note=note)

        note.title = title
        note.content = content

        db.session.add(note)
        db.session.commit()

        return redirect(url_for("notes.show", note_id=note.id))

    return render_template("notes/edit.html", categories=categories, note=note)


@notes_blueprint.route("/<int:note_id>/remove")
def remove(note_id):
    note = Note.query.get_or_404(note_id)

    db.session.delete(note)
    db.session.commit()

    return redirect(url_for("notes.index"))
