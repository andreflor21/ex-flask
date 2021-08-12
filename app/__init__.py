from flask import Flask, request, send_from_directory

app = Flask(__name__)


def escrever(conteudo):
    with open("./files/exemple.txt", "a") as f:
        f.write(conteudo)
        f.write("\n")


@app.route("/lista", methods=["POST"])
def cadastrar():
    data = request.get_json()
    quantidade = data.get("quantidade")
    item = data.get("item")

    conteudo = f"Devo comprar {quantidade} de {item}"
    escrever(conteudo)

    return {"message": "Item adicionado a lista!"}, 201


@app.route("/download/lista")
def download():
    return send_from_directory(
        directory="../files", path="exemple.txt", as_attachment=True
    )


@app.route("/upload/<filename>", methods=["POST"])
def post_file(filename):
    with open(f"./{filename}", "wb") as f:
        f.write(request.data)

    # o modo "wb" no open  é o modo escrita de binario.
    # o f"./{filename}" é o local onde sera salvo o arquivo
    # o request.data é o arquivo enviado para o upload
    return {"msg": "Upload realizado com sucesso!"}, 201


@app.route("/upload", methods=["POST"])
def post_files():
    import os

    arquivos = request.files
    primeiro_arquivo = request.files["file"]
    segundo_arquivo = request.files["file2"]

    print(primeiro_arquivo)
    print(segundo_arquivo)
    # primeiro_arquivo.save(f"/home/andre/Pictures/{primeiro_arquivo.filename}") ou
    primeiro_arquivo.save(
        os.path.join("/home/andre/Pictures", primeiro_arquivo.filename)
    )
    novo_nome = "curriculo-flask.pdf"
    segundo_arquivo.save(f"/home/andre/Documents/{novo_nome}")
    return {"msg": "Upload realizado com sucesso!"}, 201
