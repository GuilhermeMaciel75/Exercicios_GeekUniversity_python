lista = []
repetidos = []
cont = 0
for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in lista:
    cont = 0
    for y in lista:
        if x == y:
            cont += 1
    if not(x in repetidos):
        if cont >= 2:
            print(f"{x} é um valor repetido")
            repetidos.append(x)
