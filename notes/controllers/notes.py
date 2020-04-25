import typing

from flask import Blueprint, render_template

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


@notes_blueprint.route("/1", endpoint="show")
def get_one():
    db = get_db()

    note = db.get_by_id(1)

    return render_template("notes/show.html", note=note)
