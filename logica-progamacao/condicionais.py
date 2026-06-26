# umcadastro de nome, idade, nota e série.
#se o nome for igual a Eduarda, mostrar "reprovado".
#se a nota for maior que 70 e a série for "2", mstrar "reprovado".
# se a idade for menor que "18", a nota menor que 70 mostre "vá estudar".
# se o nome for "moya", idade for 22 e a nota maior ou igual a 90, mostre "sensacional".
# caso não entre em nenhuma condição, mostre "cansei, é sexta".

nome = input("digite seu nome: ")
idade = int(input("qual a sua idade?: "))
nota = float(input("digite sua nota: "))
serie = int(input("digite sua serie: "))

if nome == "eduarda":
    print("reprovado")

if nota > 70 and serie == 2:
    print("reprovado")

if idade < 18 and nota < 70:
    print("vá estudar")

if nome == "moya" and idade == 22 and nota >= 90:
    print("sensacional")

else:
    print("cansei, é sexta.")