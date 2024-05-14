from flask import flask, render_template

app = flask (__name__)

@app.route("/")
def index():
    return render_template("index.html")

from api import bp
app.register_blueprint(bp)

if __name__ == '_main_':
    app.run(host="0.0.0.0")
