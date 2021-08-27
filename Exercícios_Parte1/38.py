import random

lista = []
for x in range(10):
    n = (random.randint(0, 100))
    
    if len(lista) == 0:
        lista.append(n)
    else:
        for y in range(len(lista)):
            if n > max(lista):
                
                lista.insert(len(lista) + 1,n)

            elif n < min(lista):
                
                lista.insert(0,n)

            elif n < lista[y] and n > lista[y - 1]:
                
                lista.insert(lista.index(lista[y]),n)
                break
            

print(lista)