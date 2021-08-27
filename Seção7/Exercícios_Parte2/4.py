import random

lista = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    for j in range(4):
        lista[i][j] = random.randint(0, 100)


maior = max(lista[0])
i = 0

j = lista[0].index(maior)

for x in range(len(lista)):
    if max(lista[x]) > maior:
        maior = max(lista[x]) 
        i = x 
        j = lista[x].index(max(lista[x]))
    print(lista[x])


print(f"O maior número é o: {maior} de linha {i + 1} e coluna {j + 1}")
