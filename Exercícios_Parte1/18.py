lista = []
cont = 0

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

n = int(input("Digite um número: "))

for x in lista:

    if x % n == 0:
        cont += 1
        print(f"{x} é um múltiplo de {n}")