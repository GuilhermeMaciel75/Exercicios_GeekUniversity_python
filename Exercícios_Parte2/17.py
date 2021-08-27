notas_alunos = []

for i in range(3):
    colunas = []
    print("---------")

    for j in range(3):
        colunas.append(float(input(f"Digite a nota {j + 1} do aluno {i + 1}: ")))

    notas_alunos.append(colunas)


prova1 = 0
prova2 = 0
prova3 = 0
for x in range(len(notas_alunos)):
    if notas_alunos[x].index(min(notas_alunos[x])) == 0:
        prova1 += 1

    elif notas_alunos[x].index(min(notas_alunos[x])) == 1:
        prova2 += 1

    elif notas_alunos[x].index(min(notas_alunos[x])) == 2:
        prova3 += 1


print(f"{prova1} alunos tiveram a menor nota na Primeira Prova\n{prova2} alunos tiveram a menor nota na Segunda Prova\n{prova3} alunos tiveram a menor nota na Terceira Prova")

