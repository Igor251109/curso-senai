jogadores = []

iniciante = 0
intermediario = 0
avancado = 0

for i in range(6):
    nome = input("Nome do jogador: ")
    pontos = int(input("Pontuação: "))

    jogadores.append([nome, pontos])

    if pontos <= 20:
        iniciante += 1
    elif pontos <= 50:
        intermediario += 1
    else:
        avancado += 1

maior = jogadores[0]

for jogador in jogadores:
    if jogador[1] > maior[1]:
        maior = jogador

print("\nMaior pontuação:")
print(maior[0], "com", maior[1], "pontos")

print("\nQuantidade por nível:")
print("Iniciante:", iniciante)
print("Intermediário:", intermediario)
print("Avançado:", avancado)
