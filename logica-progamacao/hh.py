nome = input("qual seu nome?: ")
idade = int(input("qual sua idade?: "))
tem_cnh = input("tem CNH? (s/n): ")

if (idade >= 18 and nome == "luiz") or tem_cnh == "s":
    print("liberado")

elif (idade < 18 and nome == "igor"):
    print("preso")

else:
    print("multa.")