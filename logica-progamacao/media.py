num1 = float(input("digite um número: "))
num2 = float(input("digite um número: "))
num3 = float(input("digite um número: "))

media = (num1 + num2 + num3) / 3

if media >= 70:
    print(f"você está acima da media! sua média é: {media}")

elif media >= 50 and media < 69:
    print(f"recuperação! sua média é: {media}")

else:
    print(f"reprovado. sua média é: {media}")