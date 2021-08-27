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

print(f"Do vetor par {pares}, foram utilizados {len(pares)} elementos")
print(f"Do vetor impar {impar}, foram utilizados {len(impar)} elementos")

