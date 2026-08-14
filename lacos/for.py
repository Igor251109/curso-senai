contador = 0

maior = 0
menor = 100

while contador < 9:
    numero = int(input("digite um numero inteiro: "))
    contador += 1

    if numero > maior:
        maior = numero
    
    elif numero < menor:
        menor = numero

print(f"maior numero: {maior}")
print(f"menor numero: {menor}")
