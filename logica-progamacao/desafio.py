saque = float(input("qual o valor do saque que deseja fazer?: "))
saldo = float(input("qual o valor do saldo atual?: "))

if saldo >= saque:
    print("\n ==== SISTEMA BANCÁRIO ====")
    sub = saldo - (saque + 2)
    print(f"Saque concluido! o saldo atual agora é: R$ {sub}")

else:
    print("\n ==== SISTEMA BANCÁRIO ====")
    print("saque cancelado. saldo indisponivel.")

