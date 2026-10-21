import json

produto = {
        "nome": input("digite o nome do produto: ").lower().title(),
        "preço": float(input("digite o valor do produto: ")),
        "quantidade_estoque": int(input("qual a quantidade desse produto em estoque?: ")),
        "categoria": input("digite qual a categoria desse produto: ").lower().title()
    }

with open("produtos.json", 'a', encoding="utf-8") as arquivo:
    json.dump(produto, arquivo, ensure_ascii=False,  indent=4 )
