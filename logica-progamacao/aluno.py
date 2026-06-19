print("\n ==== PROCURA DE ALUNOS E MATERIA ==== ")
nome = input("qual o nome do aluno?: ")
turma = input("qual a turma do aluno?: ")
materia = input("qual a matéria que deseja ver?: ")
professor = input("qual o professor responsável?: ")

print("\n ==== NOTAS ====")
n1 = int(input("qual a primeira nota tirada na matéria?: "))
n2 = int(input("qual o segunda nota tirada na matéria?: "))
n3 = int(input("qual o terceira nota tirada na matéria?: "))

media = (n1 + n2 + n3) /3

print("\n ==== RESULTADO FINAL ====")
print("nome do aluno: ", nome)
print("turma do aluno: ", turma)
print("matéria: ", materia)
print("professor responsável: ", professor)
print("média anual: ", media)