lista = []

for _ in range(5):
    lista.append(int(input("Digite um valor: ")))

print(lista)

for x in range(lista.count(0)):
    lista.remove(0)

print(lista)
