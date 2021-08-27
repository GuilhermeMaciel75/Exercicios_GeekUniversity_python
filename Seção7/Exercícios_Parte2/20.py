import random

matriz3x6 = []

for i in range(3):
    coluna = []

    for j in range(6):
        coluna.append(random.randint(0, 100))

    matriz3x6.append(coluna)


for j in range(6):
    soma = 0
    for i in range(3):
        if j == 0 or j==2 or j==4:
            soma += matriz3x6[i][j]
            

    if soma > 0:        
        print(f"A soma dos elementos da coluna {j + 1} é igual a {soma}")

soma2 = 0
for j in range(6):
    for i in range(3):
        if j == 1 or j == 3:
            soma2 += matriz3x6[i][j]
            

print(f"A soma das colunas 2 e 4 é {soma2}")

for x in range(3):
    
    matriz3x6[x][5] = matriz3x6[x][0] + matriz3x6[x][1]

for x in range(len(matriz3x6)):
    print(matriz3x6[x])