contador = 0
notas = []

while contador != 5:
    valor = float(input("Quantas estrelas deseja dar ao restaurante? (digite de 1  a 5): "))
    if valor >= 1 and valor <= 5:
        notas.append(valor)

        contador += 1
    else:
        print("nota inválida")

total = 0
for nota in notas:
    total += nota

print(f" A média total das avaliações do produto é: {total / 5}")