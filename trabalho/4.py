contador = 0

baixo = []
zerado = []
regular = []
alto = []

while contador != 5:
    nome_produto = input("digite o nome do produto: ")
    produto = int(input("quantas unidades restantes?: "))

    if  produto == 0:
        print("-" * 20)
        print("estoque zerado.")
        zerado.append(produto)
        baixo.append(nome_produto)
    
    elif produto >= 1 and produto <= 10:
        print("-" * 20)
        print("ta acabando!")
        baixo.append(produto)
        baixo.append(nome_produto)
    
    elif produto >= 11 and produto <= 50:
        print("-" * 20)
        print("estável.")
        regular.append(produto)
        regular.append(nome_produto)

    else:
        print("-" * 20)
        print("ta sobrando.")
        alto.append(produto)
        alto.append(nome_produto)
    
    contador += 1

print(f"os produtos zerados são: {zerado} e são um total de {len(zerado)} produtos.")
print("-" * 20)
print(f"os produtos que estão acabando são: {baixo} e são {len(baixo)} produtos.")
print("-" * 20)
print(f"os produtos que estão regulares são: {regular} e são {len(regular)} produtos.")
print("-" * 20)
print(f"os produtos que estão sobrando são: {alto}, e são {len(alto)} produtos.")