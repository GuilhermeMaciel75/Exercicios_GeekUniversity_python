lista = []
repetidos = []

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in lista:
    if lista.count(x) > 1 and not(x in repetidos):
        print(f'{x} é um valor repetido')
        repetidos.append(x)

