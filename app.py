from flask import flask, render_template

app = flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

from api import bp
app.register_blueprint(bp)