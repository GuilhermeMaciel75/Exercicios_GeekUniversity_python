import random

matriz3 = []

for i in range(3):
    coluna = []

    for j in range(3):
        coluna.append(random.randint(0, 100))

    matriz3.append(coluna)

soma = 0

for i in range(3):
    for j in range(3):
        if i < j:
            soma += matriz3[i][j]

print(f"A soma é {soma}")

for x in range(len(matriz3)):
    print(matriz3[x])
