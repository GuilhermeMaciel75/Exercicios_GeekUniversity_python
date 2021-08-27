import random

lista = []

for _ in range(10):
    lista.append(random.randint(0, 100))

print(lista)

for i in lista:
    cont = 0
    for j in range (1, i):
        if i % j == 0:
            cont += 1
    
    if cont < 2:
        print(f"{i} é primo e sua posição é {lista.index(i)}")