numero = 0
tabuada = []

while True:
    numero_pedido = int(input("digite seu número: "))
    tabuada.append(numero_pedido)

    for num in tabuada:
        print(num * 1)
        print("-" * 20)

        print(num * 2)
        print("-" * 20)

        print(num * 3)
        print("-" * 20)

        print(num * 4)
        print("-" * 20)

        print(num * 5)
        print("-" * 20)

        print(num * 6)
        print("-" * 20)

        print(num * 7)
        print("-" * 20)

        print(num * 8)
        print("-" * 20)

        print(num * 9)
        print("-" * 20)

        print(num * 10)
        print("-" * 20)

    quer_mais = input("quer saber mais alguma taboada?: ")

    if quer_mais == "s" or quer_mais == "sim" or quer_mais == "SIM":
        numero_pedido = int(input("digite seu número: "))
        tabuada.append(numero_pedido)

        for num in tabuada:
            print(num * 1)
            print("-" * 20)

            print(num * 2)
            print("-" * 20)

            print(num * 3)
            print("-" * 20)

            print(num * 4)
            print("-" * 20)

            print(num * 5)
            print("-" * 20)

            print(num * 6)
            print("-" * 20)

            print(num * 7)
            print("-" * 20)

            print(num * 8)
            print("-" * 20)

            print(num * 9)
            print("-" * 20)

            print(num * 10)
            print("-" * 20)
        
    else:
        break