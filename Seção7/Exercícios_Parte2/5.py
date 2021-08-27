import random

lista = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        lista[i][j] = random.randint(0, 100)


for x in range(len(lista)):

    print(lista[x])


valor = int(input("Valor para ser procurado na matriz: "))


achou = False
for i in range(5):
    for j in range(5):
        if lista[i][j] == valor:
            print(f"Valor encontrado, linha: {i + 1} e coluna: {j + 1}")
            achou = True


if achou == False:
    print("Valor não encontrado")
            
            