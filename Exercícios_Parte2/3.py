
lista = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    for j in range(4):
        lista[i][j] = (i + 1) * (j + 1)

for x in range(len(lista)):

    print(*lista[x])
