import random

matriz3 = []

for i in range(3):
    coluna = []

    for j in range(3):
        coluna.append(random.randint(0, 100))

    matriz3.append(coluna)

print("Matriz Normal:")
for x in range(len(matriz3)):
    print(matriz3[x])

matriz3_nova = []
for i in range(3):
    coluna = []

    for j in range(3):
        coluna.append(matriz3[j][i])

    matriz3_nova.append(coluna)

print("-------------\nMatriz Transposta:")
for x in range(len(matriz3_nova)):
    print(matriz3_nova[x])