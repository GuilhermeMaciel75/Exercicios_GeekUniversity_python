import random

lista = []

for _ in range(11):
    lista.append(random.randint(0, 100))

print(lista)
    
lista_nova = []
for x in range (5):
    lista_nova.append(min(lista))
    lista.pop(lista.index((min(lista))))


for x in range (6):
    lista_nova.append(max(lista))
    lista.pop(lista.index((max(lista))))

print(lista_nova)
