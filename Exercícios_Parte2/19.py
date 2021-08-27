notas = []

for i in range(5):
    
    coluna = []

    coluna.append(int(input(f"Mátrícula do Aluno {i + 1}: ")))
    prova = int(input(f"Média das provas do Aluno {i + 1}: "))
    coluna.append(prova)
    trabalhos = int(input(f"Média dos trabalhos do Aluno {i + 1}: "))
    coluna.append(trabalhos)
    coluna.append(prova + trabalhos)

    notas.append(coluna)
    

soma = 0
maior = 0
for x in range(len(notas)):
    soma += notas[x][3]

    if notas[x][3] > maior:
        maior = notas[x][3]
        indice = x


print(f"A maior nota foi do aluno {notas[indice][0]}")