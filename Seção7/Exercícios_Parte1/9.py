lista = []

for _ in range(6):
    n = int(input("Dige um número: "))
    while(n % 2 != 0):
        n = int(input("Valor não par, Dige outro número: "))
    lista.append(n)

for x in lista[::-1]:
    print(x)