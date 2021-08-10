# iniciando com flask
# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# # @app.route('/', methods=['GET']) se quiser deixar claro qual o metodo HTTP
# def home():
#     return "Bem vindo ao Flask!"

# variaveis de ambiente

from flask import Flask
from environs import Env
from os import environ

env = Env()
env.read_env()

app = Flask(__name__)


@app.route("/")
def home():
    # pegando a variavel user do env
    user = environ.get("user")
    return f"Bem vindo ao Flask {user}"
