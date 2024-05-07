from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)

#Daqui pra baixo as rotas

@bp.route("/api", methods=("GET",))
def index():
    return jsonify({"status": 200; "mensagem": "API de Maria Laura"})

@bp.route("/api/aleatorios") # decorator de rotas
def aleatorios(): # função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/api/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome })

@bp.route("/api/argumentos", methods=("GET",))
def arg_implicito(nome: str):
    return jsonify({"status": 200, "data": nome })

@bp.route("/api/idades", methods=("GET, "))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

@bp.route("/api/salarios", methods=("GET,"))
def salarios():
    from random_data import salarios
    import funcoes
    num = funcoes.mais_2000(salarios)
    return jsonify({"status": 200, "data": num })

@bp.route("/api/maiores_salarios", methods=("GET,"))
def maiores_salarios():
    from random_data import maiores_salarios
    import funcoes
    num = funcoes.maior_salario(maiores_salarios)
    return jsonify({"status": 200, "data": num })

@bp.route("/api/media_profissoes", methods=("GET,"))
def media_profissoes():
    from random_data import media_profissoes
    import funcoes
    num = funcoes.media_profissoes(media_profissoes)
    return jsonify({"status": 200, "data": num})

@bp.route("/api/intervalo_idades_mais2000_sexo", methods=("GET, "))
def intervalo_idades_mais200_sexo():
    from random_data import intervalo_idades_mais2000_sexo
    import funcoes
    num = funcoes.maior_2000_sexo(intervalo_idades_mais2000_sexo)
    return jsonify({"status": 200, "data": num})
