num1 = float(input("digite o valor da compra: "))

if num1 >= 100:
    desconto = num1 * 0.10
    total = num1 - desconto
    print(f"desconto aplicado! de R${num1},  sua compra deu o total de: R$ {total}")

else:
    print(f"sua compra deu o total de: R${num1}")