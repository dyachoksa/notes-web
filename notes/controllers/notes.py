import typing

from flask import Blueprint

from ..db import get_db
from ..models import Note


notes_blueprint = Blueprint("notes", __name__)


def format_notes(notes: typing.List[Note]):
    return [dict(id=note.id, title=note.title, content=note.content) for note in notes]


@notes_blueprint.route("/", endpoint="index")
def get_list():
    db = get_db()
    notes = db.get_notes()

    output = ["<ul>"]

    for note in notes:
        output.append(f"<li>{note.id}: {note.title}</li>")

    output.append("</ul>")

    return "".join(output)


@notes_blueprint.route("/1", endpoint="show")
def get_one():
    db = get_db()

    note = db.get_by_id(1)

    return note.content
