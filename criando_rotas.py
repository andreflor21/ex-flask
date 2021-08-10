from flask import Flask, json, request, jsonify

app = Flask(__name__)

lista_de_nomes = [{"nome": "Elon Musk", "nome": "Bill Gates"}]


@app.route("/nomes", methods=["GET"])
def todos_nomes():
    return jsonify(lista_de_nomes), 200
