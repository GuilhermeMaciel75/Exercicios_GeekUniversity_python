import random

matriz3 = []

for i in range(3):
    coluna = []

    for j in range(3):
        coluna.append(random.randint(0, 100))

    matriz3.append(coluna)

soma_colunas = []

for x in range(len(matriz3)):
    print(matriz3[x])

for i in range(3):
    linha = 0
    soma = 0
    while(linha <= 2):
        soma += matriz3[linha][i]
        linha += 1
    soma_colunas.append(soma)
    
print(*soma_colunas)
