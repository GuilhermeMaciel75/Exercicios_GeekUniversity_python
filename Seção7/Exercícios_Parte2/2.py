import random

lista = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
cont = 0

for i in range(5):
    for j in range(5):
        if i == j:
            lista[i][j] = 1
        else:
            lista[i][j] = 0


for x in range(len(lista)):

    print(lista[x])
