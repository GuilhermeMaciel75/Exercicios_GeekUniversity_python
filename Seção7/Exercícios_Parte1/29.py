import random

lista = []

for _ in range(10):
    lista.append(random.randint(0, 100))
    #lista.append(input("Digite um valor: "))

print(lista)
pares = []
impar = []

for x in lista:

    if x % 2 == 0:
        pares.append(x)

    else:
        impar.append(x)

print(f"Números pares digitados: {pares}")
print(f"A soma dos numéros pares é {sum(pares)}")
print(f"Números Impares digitados: {impar}")
print(f"O número de ímpares digitados é {len(impar)}")
