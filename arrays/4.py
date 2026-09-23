turmas = ["1º Ano A", "1º Ano B", "2º Ano A", "2º Ano B", "3º Ano A", "3º Ano B"]
primeiros_anos = []
terceiros_anos = []

print(f"a posição do 2º ano B é: {turmas.index("2º Ano B")}")

lista = turmas[0:1]
lista2 = turmas[-2:-1]

primeiros_anos.append(lista)
terceiros_anos.append(lista2)

print(f"todas as turmas: {turmas}")
print(f"terceiros anos: {terceiros_anos}")
print(f"primeiros anos: {primeiros_anos}")