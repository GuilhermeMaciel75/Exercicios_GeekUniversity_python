import random

matriz3 = []

for i in range(3):
    coluna = []

    for j in range(3):
        coluna.append(random.randint(0, 100))

    matriz3.append(coluna)

soma = 0

controle1 = 3
controle2 = 1

for i in range(3):
    for j in range(3):
        if (i + 1) == controle2 and (j + 1) == controle1:
            print(matriz3[i][j])
            soma += matriz3[i][j]
            controle1 -= 1
            controle2 += 1 

print(f"A soma é {soma}")

for x in range(len(matriz3)):
    print(matriz3[x])
