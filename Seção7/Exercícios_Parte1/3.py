lista = []

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

quadrado = []


for x in lista:
    x = x ** 2
    quadrado.append(x)

print(lista)
print(quadrado)

