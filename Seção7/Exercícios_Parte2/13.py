import random

matriz4 = []

for i in range(4):
    coluna = []

    for j in range(4):
        coluna.append(random.randint(1, 20))

    matriz4.append(coluna)

for x in range(len(matriz4)):
    print(matriz4[x])

for i in range(4):
    for j in range(4):
        if i > j:
            matriz4[i][j] = 0

print("-------------\nMatriz Triangular:")
for x in range(len(matriz4)):
    print(matriz4[x])