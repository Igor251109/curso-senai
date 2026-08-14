idade = int(input("digite sua idade: "))

while idade > 0:
    if idade > 0 and idade < 13:
        print("você é criança.")
        break
    elif idade >= 13 and idade < 18:
        print("você é adolecente.")
        break
    elif idade >= 18 and idade < 60:
        print("você é adulto.")
        break
    elif idade >= 60 and idade < 121:
        print("você é idoso.")
        break
    else:
        print("ou você ta comprindo hora extra ou é um extraterrestre.")
        break