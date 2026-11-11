'''
import sqlite3
import json

arquivo_json = "clientes.json"

produto = {
    "nome": input("Digite seu nome: ").strip().lower(),
    "email": input("Digite seu email: ").strip().lower(),
    "idade": int(input("digite sua idade: "))
}

try:
    with open(arquivo_json, 'r', encoding="utf-8") as arquivo:
        lista = json.load(arquivo)
        print('-' * 50)
        lista.append(produto, arquivo)
    
    
except:
    lista = []
    lista.append(produto)
'''


import sqlite3
import json

arquivo_json = "clientes.json"

produto = {
    "id": int(input("digite seu id: ")),
    "nome": input("Digite seu nome: ").strip().lower(),
    "email": input("Digite seu email: ").strip().lower(),
    "idade": int(input("digite sua idade: "))
}

try:
    with open(arquivo_json, 'r', encoding="utf-8") as arquivo:
        lista = json.load(arquivo)
        print('-' * 50)

        lista.append(produto)
        
        with open(arquivo_json, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    
    
except:
    lista = []
    lista.append(produto)
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


        

def migrar_json_para_sqlite(caminho_json):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            nome_cliente TEXT NOT NULL,
            email_cliente TEXT NOT NULL,
            idade_cliente INTEGER NOT NULL
        )
    ''')

    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        clientes = json.load(arquivo)

    dados = []

    for cliente in clientes:
        dados.append((cliente["id"], cliente["nome"], cliente["email"], cliente["idade"]))

    cursor.executemany('''
        INSERT INTO clientes
        (id_cliente, nome_cliente, email_cliente, idade_cliente)
        VALUES (?, ?, ?, ?)
    ''', dados)

    conexao.commit()
    conexao.close()

    print("Migração concluída com sucesso!")

migrar_json_para_sqlite(arquivo_json)