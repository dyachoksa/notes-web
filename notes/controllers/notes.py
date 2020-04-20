from flask import Blueprint, jsonify

notes_blueprint = Blueprint("notes", __name__)


@notes_blueprint.route("/", endpoint="index")
def get_list():
    notes = [
        {"id": 1, "title": "First note", "content": "First note content"},
    ]

    return jsonify(notes)


@notes_blueprint.route("/1", endpoint="show")
def get_one():
    return "Note"
