'''
Exercício 03: Gerador de Lista de Compras (.writelines())
Crie uma lista vazia chamada compras.
Utilize um laço for para solicitar que o usuário digite 5 itens de supermercado, adicionando cada item à lista compras já com o caractere \n ao final.
Abra um arquivo chamado "lista_compras.txt" no modo "w".
Escreva todos os itens de uma vez só utilizando o método .writelines(compras).
Exiba na tela: "Lista de compras gerada com sucesso!".
'''

lista = []
item_mercado = input("digite um item que precisa do mercado: ").strip().title()
contador = 0

with open("lista_compras.txt", "w", encoding="utf-8") as arquvo:
    for item in lista:
        lista.append(f"{item_mercado}\n")
        contador