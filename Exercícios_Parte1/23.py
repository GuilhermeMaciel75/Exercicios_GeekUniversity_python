import random

lista1 = []
lista2 = []
lista3 = []

soma = 0

for _ in range(5):
    lista1.append(random.randint(0, 100))
    lista2.append(random.randint(0, 100))

for x in range(len(lista1)):
    soma = soma + (lista1[x] * lista2[x])

print(lista1)
print(lista2)
print(soma)