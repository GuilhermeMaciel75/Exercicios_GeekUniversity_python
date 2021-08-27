import random

lista1 = set({})
lista2 = set({})
lista3 = set({})
lista4 = set({})



for _ in range(5):
    lista1.add(random.randint(0, 100))
    lista2.add(random.randint(0, 100))


for x in range(len(lista1)):
    lista3.add(list(lista1)[x] + list(lista2)[x])
    lista4.add(list(lista1)[x] * list(lista2)[x])
    lista4.add(list(lista1)[x] - list(lista2)[x])

intersercao = lista1.intersection(lista2)
uniao = lista1.union(lista2)

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(intersercao)
print(uniao)



