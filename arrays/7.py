turma_manha = ["Lucas", "Mariana", "Pedro"]
turma_tarde = ["Gabriel", "Sofia", "Lucas", "Beatriz"]
turma_completa = []

for aluno in turma_manha:
    if aluno in turma_completa:
        pass
    else:
        turma_completa.append(aluno)

for aluno in turma_tarde:
    if aluno in turma_completa:
        pass
    else:
        turma_completa.append(aluno)

print(turma_completa)