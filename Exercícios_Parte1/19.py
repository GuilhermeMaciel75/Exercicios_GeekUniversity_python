lista = []

for x in range(50):
   lista.append((x + 5 * x) % (x + 1))

print(lista)