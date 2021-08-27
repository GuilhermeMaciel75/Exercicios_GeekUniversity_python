lista = []

for _ in range(5):
    n = int(input("Dige um número: "))
    lista.append(n)

print(f"O Maior valor da lista: lista[{lista.index(max(lista))}] = {max(lista)}\n\
O menor valor da lista: lista[{lista.index(min(lista))}] = {min(lista)}")