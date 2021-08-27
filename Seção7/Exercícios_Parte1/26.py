
import random

lista = []
soma = 0
for _ in range(10):
    lista.append(random.randint(0, 100))

media = sum(lista)/len(lista)

for x in lista:
    soma = soma + ((x - media) ** 2)

print(soma)
resultado = (soma / 9) ** 0.5

print(f"O desvio padrão do vetor : {lista} é {resultado:.2f}")

'''

lista = []
soma = 0
for a in range(10):
    lista.append(input(f"Digite o {a + 1} da lista: "))

media = sum(lista)/len(lista)

for x in lista:
    soma = soma + ((x - media) ** 2)

print(soma)
resultado = (soma / 9) ** 0.5

print(f"O desvio padrão do vetor : {lista} é {resultado:.2f}")
'''