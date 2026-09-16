senha_correta = 67
contador = 0

while True:
    senha = int(input("digite sua senha: "))

    if senha_correta > senha:
        print("sua senha é menor que esse número.")
    
    elif senha_correta < senha:
        print("sua senha é maior que esse número.")
    
    elif senha_correta == senha:
        print(f"senha correta! Bem vindo, Maconheiro! as suas tentativas foram : {contador}")
        break

    contador += 1