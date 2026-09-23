fila = ["Ana", "Carlos", "Beatriz", "Daniel"]
print(fila)
print("-" * 30)

fila.append("eduardo")
print(fila)
print("-" * 30)

print(f"atendendo o aluno: {fila[0]}")
fila.pop(0)
print(fila)
print("-" * 30)

fila.remove("Beatriz")

print(f'''O resultado final da lista é: 
      {fila}''')