lista = []

for _ in range(8):
    n = int(input("Dige um número: "))
    lista.append(n)

x = int(input("Diga um valor de 0 - 9: "))
y = int(input("Diga um valor de 0 - 9: "))

soma = lista[x] + lista[y]

print(f'lista[{x}] + lista[{y}] => {lista[x]} + {lista[y]} = {soma}')