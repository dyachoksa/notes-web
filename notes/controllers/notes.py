import typing

from flask import Blueprint, render_template, abort, request, redirect, url_for

from ..db import get_db
from ..models import Note


notes_blueprint = Blueprint("notes", __name__)


def format_notes(notes: typing.List[Note]):
    return [dict(id=note.id, title=note.title, content=note.content) for note in notes]


@notes_blueprint.route("/", endpoint="index")
def get_list():
    db = get_db()
    notes = db.get_notes()

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
            title=title, content=content
        )

        db = get_db()
        db.create(note)

        return redirect(url_for("notes.show", note_id=note.id))

    return render_template("notes/create.html", title="", content="")


@notes_blueprint.route("/<int:note_id>", endpoint="show")
def get_one(note_id):
    db = get_db()

    note = db.get_by_id(note_id)
    if note is None:
        return abort(404)

    return render_template("notes/show.html", note=note)


@notes_blueprint.route("/<int:note_id>/edit", methods=["GET", "POST"])
def edit(note_id):
    db = get_db()

    note = db.get_by_id(note_id)
    if note is None:
        return abort(404)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if len(title) < 3 or len(content) < 3:
            error = "Please check your form. All fields are required."

            note.title = title
            note.content = content

            return render_template("notes/edit.html", error=error, note=note)

        note.title = title
        note.content = content

        db.update(note)

        return redirect(url_for("notes.show", note_id=note.id))

    return render_template("notes/edit.html", note=note)


@notes_blueprint.route("/<int:note_id>/remove")
def remove(note_id):
    db = get_db()

    note = db.get_by_id(note_id)
    if note is None:
        return abort(404)

    db.delete(note)

    return redirect(url_for("notes.index"))
