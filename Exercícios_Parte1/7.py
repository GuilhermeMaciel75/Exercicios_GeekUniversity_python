lista = []

for _ in range(10):
    n = int(input("Dige um número: "))
    lista.append(n)



print(f'O valor maxímo dessa lista é {max(lista)} sua posição é lista[{lista.index(max(lista))}]')