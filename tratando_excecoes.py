from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def soma():
    try:
        valores = request.get_json()
        v1 = valores.get("valor1")
        v2 = valores.get("valor2")
        soma = v1 + v2
        return {"valor1": v1, "valor2": v2, "resultado": soma}, 201
    except TypeError as err:
        return {"msg": f"{err}"}, 400


# EAFP vs LBYL
# EAFP == é mais fácil pedir perdão do que permissão
# LBYL == olhe antes de pular // look before you leap

# LBYL
# verificando se a chave nome existe no dicionario
meu_dict = {}
if "nome" in meu_dict:
    print(meu_dict["chave"])

# EAFP
# No EAFP primeiro você tenta, caso dê errado, trata no EXCEPT
try:
    print(meu_dict["chave"])
except KeyError as _:
    # por hora iremos somente passar
    ...


# tipos de erros mais frequentes:
# SyntaxError, IndexError, NameError
