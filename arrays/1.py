nomes = []
contador = 0

while contador != 5:
    nome = input("digite o nome que deseja adicionar na lista: ").strip().title()

    if nome in nomes:
        print("o nome já está na lista.")
        continue

    else:
        nomes.append(nome)
        print("nome adicionado com sucesso.")
    
    contador += 1