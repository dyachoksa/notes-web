from flask import jsonify

from .. import app


@app.route("/")
def index():
    return """
<html>
<head>
    <title>Notes App</title>
</head>
<body>
    <h1>Notes Application</h1>
</body>
</html>
    """


@app.route("/notes")
def notes():
    notes = [
        {"id": 1, "title": "First note", "content": "First note content"},
    ]

    return jsonify(notes)
