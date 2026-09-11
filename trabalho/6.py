senha = 67      # six seven é a droga de hoje em dia.
usuario = "drogas"    # usuáros usam drogras

contador = 0

while contador != 3:
    nome = input("digite o nome de login: ")
    sua_senha = int(input("digite sua senha numérica: "))

    if nome == usuario and sua_senha == senha:
        print("Bem vindo, maconheiro!")
        break
    
    else:
        print("caia fora! Sistema de segurança contra drogados ativado.")
    
    contador += 1
