print("\n ==== CALCULADORA DE DOENTE ====")

print(1, 2, 3)
print(4, 5, 6)
print(7, 8, 9)
print("=", 0, "sair")
print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")

opcao = input("digite uma opção: ").lower()

while opcao != "sair":
    if opcao == "somar":
        n1 = int(input("digite o primeiro numero: "))
        n2 = int(input("digite o segundo numero: "))

        total = n1 + n2
        print(f"a soma total é: {total}")

        print("\n ==== CALCULADORA DE DOENTE ====")

        print(1, 2, 3)
        print(4, 5, 6)
        print(7, 8, 9)
        print("=", 0, "sair")
        print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")
        opcao = input("digite uma opção: ").lower()
    
    elif opcao == "subtrair":
        n1 = int(input("digite o primeiro numero: "))
        n2 = int(input("digite o segundo numero: "))

        total = n1 - n2
        print(f"a subtração total é: {total}")

        print("\n ==== CALCULADORA DE DOENTE ====")

        print(1, 2, 3)
        print(4, 5, 6)
        print(7, 8, 9)
        print("=", 0, "sair")
        print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")
        opcao = input("digite uma opção: ").lower()
    
    elif opcao == "multiplicar":
        n1 = int(input("digite o primeiro numero: "))
        n2 = int(input("digite o segundo numero: "))

        total = n1 * n2
        print(f"a multiplicão total é: {total}")

        print("\n ==== CALCULADORA DE DOENTE ====")

        print(1, 2, 3)
        print(4, 5, 6)
        print(7, 8, 9)
        print("=", 0, "sair")
        print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")
        opcao = input("digite uma opção: ").lower()
    
    elif opcao == "divisao":
        n1 = int(input("digite o primeiro numero: "))
        n2 = int(input("digite o segundo numero: "))

        if n2 == 0:
            print("resultado igual a 0.")
    
        total = n1 / n2
        print(f"a divisão total é: {total}")

        print("\n ==== CALCULADORA DE DOENTE ====")

        print(1, 2, 3)
        print(4, 5, 6)
        print(7, 8, 9)
        print("=", 0, "sair")
        print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")
        opcao = input("digite uma opção: ").lower()

    else:
        print("opção inválida. try again.")

        print("\n ==== CALCULADORA DE DOENTE ====")

        print(1, 2, 3)
        print(4, 5, 6)
        print(7, 8, 9)
        print("=", 0, "sair")
        print("OPÇÕES: SOMAR || SUBTRAIR || MULTIPLICAR || DIVIDIR || SAIR ||")
        opcao = input("digite uma opção: ").lower()