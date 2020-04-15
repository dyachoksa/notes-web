from . import app, controllers

app.add_url_rule("/", "index", controllers.index)
app.add_url_rule("/notes", "notes", controllers.notes)
