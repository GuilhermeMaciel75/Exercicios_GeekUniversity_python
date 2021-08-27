lista = []
pares = 0

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in lista:
    if x % 2 == 0:
        print(x)
        pares += 1

print(f"Essa lista possui {pares} pares")
