adulto = []
idoso = []
adolescente = []
crianca = []

contador = 0

while contador != 10:
    idade = int(input("digite sua idade: "))

    if idade <= 13 and idade >= 0:
        print("você é criança.")
        print("-" * 20)
        crianca.append(idade)
    
    elif idade > 13 and idade <= 17:
        print("você é adolescente.")
        print("-" * 20)
        adolescente.append(idade)
    
    elif idade > 17 and idade < 60:
        print("você é adulto.")
        print("-" * 20)
        adulto.append(idade)
    
    else:
        print("você é idoso.")
        print("-" * 20)
        idoso.append(idade)
    
    contador += 1

print(f"o número de crianças é: {len(crianca)} pessoas.")
print("-" * 20)
print(f"o número de adlescentes é: {len(adolescente)} pessoas.")
print("-" * 20)
print(f"o número de idosos é: {len(adulto)} pessoas.")
print("-" * 20)
print(f"o número de idosos é: {len(idoso)} pessoas.")