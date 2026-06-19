print("\n ==== QUESTIONÁRIO DE ROTINA ====")
nome = input("qual o nome do prestador de serviço?: ")
telefone = input("qual o telefone do prestador de serviço?: ")
cpf = input("qual o CPF do prestador e serviço?: ")
salario = float(input("qual o salário atual do prestador de serviço?: "))

salario_anual = salario * 12

print("nome:", nome)
print("telefone: ", telefone)
print("CPF: ", cpf)
print("salário: ", salario)
print("salario anual: ", salario_anual)