# para abrir um arquivo
f = open("text.txt")
# para fechar um arquivo
f.close()


# Manipulando o arquivo
# leitura
with open("text.txt", "r") as f:
    leitura = f.read()
    print(leitura)
# escrita
with open("text.txt", "w") as f:
    escrita = f.write("ALOU")
    print(escrita)
# com o parametro "w" ele sobrescreve todo arquivo text.txt para adicionar ao final dele utilize "a" de append
with open("text.txt", "a") as f:
    escrita = f.write("\nSALVE BR")
    print(escrita)

# escrever varias linhas
with open("text.txt", "w") as f:
    conteudo = [
        "A mala nada na lama\n",
        "A grama é amarga\n",
        "O lobo ama o bolo\n",
        "Luz azul\n",
    ]
    escrita = f.writelines(conteudo)
    print(escrita)

# padrao de leitura em arquivos
with open("text.txt", "r") as f:
    for linha in f:
        print(linha)
