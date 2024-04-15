from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": 200, "message": "API de MARIA_LAURA_BONFIM_MEASSO"})
@app.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})
if __name__ == '_main_':
    app.run(debug=True)
@app.route("/argumentos/string:nome>")
def argumentos(nome: str):
    return jsonify({"status"})