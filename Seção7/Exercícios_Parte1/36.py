lista = []

for _ in range(10):
    lista.append(int(input("Digite um valor: ")))

print(sorted(lista))

for x in range(len(lista)):
    print(lista[x])