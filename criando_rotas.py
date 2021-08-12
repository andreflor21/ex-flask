from flask import Flask, json, request, jsonify

app = Flask(__name__)

lista_de_nomes = [{"nome": "Elon Musk"}, {"nome": "Bill Gates"}]


@app.route("/nomes", methods=["GET", "POST"])
def registrar_listar_nomes():
    if request.method == "POST":
        req = request.get_json()
        novo_nome = req.get("nome")
        lista_de_nomes.append(req)

        return {"msg": f"Usuário {novo_nome} cadastrado!"}, 201

    return jsonify(lista_de_nomes), 200


# url dinamicas
@app.route("/nomes/<nome>", methods=["GET"])
def buscar_nome(nome):
    """Lógica interna para busca do nome da pessoa e suas funcionalidades,
    utilizando a variável nome que vem da url
    """
    if nome:
        return {"msg": f"Olá {nome}"}

    return {"msg": "Olá fulano"}


# query params
@app.route("/testando/query_params")
def query_params_route():
    # pega todos os argumentos passados na URL
    # query_params = request.args
    nome = request.args.get("nome")

    if nome:
        return {"msg": f"Olá {nome}! Seja bem vindo! :D"}

    return {"msg": "status ok"}
    # return query_params
