lista1 = []
lista2 = []
lista3 = []

for x in range(10):
    n = int(input(f"Dige o número {x + 1} da lista1: "))
    lista1.append(n)

for y in range(10):
    n = int(input(f"Dige o número {y + 1} da lista2: "))
    lista2.append(n)

for z in range(len(lista1)):
    lista3.append(lista1[z] - lista2[z])

print(lista3)