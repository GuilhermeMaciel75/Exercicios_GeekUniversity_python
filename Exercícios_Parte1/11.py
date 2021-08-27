lista = []
negativos = 0
positivos = 0

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)

for x in lista:
    if x % 2 == 0:
        positivos += x
    else:
        negativos += 1

print(f"Essa lista possui {negativos} números negativos\nA soma de todos os positivos é {positivos}")