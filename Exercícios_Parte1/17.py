lista = []


for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in range(len(lista)):
    if lista[x] < 0:
        lista[x] = 0

print(lista)