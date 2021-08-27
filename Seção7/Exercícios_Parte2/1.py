import random

lista = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cont = 0

for i in range(4):
    for j in range(4):
        lista[i][j] = int(input(f"Digite o valor da linha{i} da coluna{j}: "))

for linhas in range(4):
    for colunas in range(4):
        if lista[linhas][colunas] > 10:
            print(lista[linhas][colunas])
            cont += 1

print(lista)
print(f"A lista possui {cont} acima do 10")
