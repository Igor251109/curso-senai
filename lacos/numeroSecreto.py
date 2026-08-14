senha = 999
senha_correta = int(input("digite sua senha: "))
tentativas = 1

while senha_correta != senha:
    tentativas += 1
    print("senha incorreta, tente novamente.")
    senha_correta = int(input("digite sua senha: "))

print("as tentativas totais foram: ", tentativas)