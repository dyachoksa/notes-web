from flask import Flask, g

from .services import NotesService


def get_db() -> NotesService:
    if "db" not in g:
        g.db = NotesService()
        g.db.load_notes()

    return g.db


def close_db(e=None):
    pass


def init_app(app: Flask):
    _ = NotesService()
    app.teardown_appcontext(close_db)
