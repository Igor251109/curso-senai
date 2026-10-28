import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()


# CRIAR TABELA NO BANCO DE DADOS

cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               preco REAL NOT NULL,
               estoque INTEGER NOT NULL
               )
               ''')

conexao.commit()





print("\nCADASTRAR PRODUTOS NO BANCO DE DADOS")

nome  = input("digite o nome do produto: ").lower().title()
preco = float(input("digite o preço do produto: "))
estoque = int(input("digite a quantidade atual do estoque: "))

cursor.execute('''INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)''',
                (nome, preco, estoque))

conexao.commit()




print("\nVER PRODUTOS CADASTRADOS")

cursor.execute('''SELECT * FROM produtos''')
produtos = cursor.fetchall()

for produto in produtos:
    print(
        f"| ID: {produto[0]} |"
        f"| NOME PRODUTO: {produto[1]} |" 
        f"| PREÇO: R${produto[2]:.2f} |"
        f"| ESTOQUE: {produto[3]}"
    )


print("\n PREÇO MAXIMO:")
preco_maximo = float(input("digite o preço maximo que você pagaria no produto: "))

if preco_maximo > 0:
    cursor.execute('''SELECT  * FROM produtos''')
    produtos = cursor.fetchall()

    for produto in produtos:
        if produto[2] <= preco_maximo:
            print(
                f"| NOME PRODUTO: {produto[1]} |"
                f"| PREÇO: {produto[2]:.2f}"
            )



print("\n VENDA:")

for produto in produtos:
    print(
        f"| ID: {produto[0]} |"
        f"| NOME PRODUTO: {produto[1]} |" 
        f"| PREÇO: R${produto[2]:.2f} |"
        f"| ESTOQUE: {produto[3]}"
    )

idx = int(input("digite o ID do produto que deseja vender: "))

cursor.execute('''SELECT * FROM produtos WHERE id = ?''', (idx,))
produto = cursor.fetchone()

if produto:
    quantos_vender = int(input("quantos produtos deseja comprar?: "))

    cursor.execute('''UPDATE produtos SET quantidade = ? WHERE id = ?''', (quantos_vender, idx))

    conexao.commit()
    conexao.close()