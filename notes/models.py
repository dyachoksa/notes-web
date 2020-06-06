import datetime as dt

from .db import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True, unique=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id", ondelete="CASCADE"), nullable=True
    )
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)

    category = db.relationship("Category", backref=db.backref("notes", lazy=True), lazy=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Note id={self.id} title={self.title}>"
