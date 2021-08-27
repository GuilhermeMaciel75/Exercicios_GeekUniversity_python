lista = []
repetidos = []

for _ in range(20):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in lista:
    if (lista.count(x) > 1 and not(x in repetidos)):
            repetidos.append(x)
    elif x not in repetidos:
        print(f'{x} não é um valor repetido')