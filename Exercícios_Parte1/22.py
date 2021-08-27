
import random

lista1 = []
lista2 = []
lista3 = []

for _ in range(10):
    lista1.append(random.randint(0, 100))
    lista2.append(random.randint(0, 100))

for x in range(len(lista1)):
    if x % 2 == 0:
        lista3.append(lista1[x])
    else:
        lista3.append(lista2[x])


print(lista1)
print(lista2)
print(lista3)

'''
Input do Usuário
lista1 = []
lista2 = []
lista3 = []

for _ in range(10):
    lista1.append(input("Informe um valor para a lista 1"))
    lista2.append(input("Informe um valor para a lista 2"))

for x in range(len(lista1)):
    if x % 2 == 0:
        lista3.append(lista1[x])
    else:
        lista3.append(lista2[x])


print(lista1)
print(lista2)
print(lista3)
'''


