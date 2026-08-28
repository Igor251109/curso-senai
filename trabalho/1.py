contador = 0

while contador != 5:
    nota = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digitesua terceira nota: "))

    media = (nota + nota2 + nota3) / 3

    if media >= 6:
        print("-" * 30)
        print("aprovado.")
        print("-" * 30)
    
    elif media >= 4 and media <= 5.9:
        print("-" * 30)
        print("recuperação.")
        print("-" * 30)
    
    else:
        print("-" * 30)
        print("reprovado.")
        print("-" * 30)
    
    contador += 1