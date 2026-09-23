alunos = [7.5, 4.0, 9.2, 5.5, 3.8, 10.0, 6.5, 2.0]
aprovados = []
reprovados = []

for aluno in alunos:
    if aluno >= 6:
        aprovados.append(aluno)
    
    elif aluno < 6:
        reprovados.append(aluno)

print("a média da turma é:", sum(alunos))
print("O número de alunos que ficaram de recuperação foram:", len(alunos))
print("O número de alunos que foram aprovados é:", len(alunos))