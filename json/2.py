import json

banco_dados = "produtos.json"

with open(banco_dados, "r", encoding="utf-8") as arquivo:
    produtos = json.load(arquivo)

    for produto in produtos:
        print(f"nome: {produto['nome']}/ preço: {produto['preço']}/ estoque: {produto["quantidade_estoque"]}")