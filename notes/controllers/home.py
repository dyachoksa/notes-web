from flask import Blueprint

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
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
