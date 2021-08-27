a = input("Digite um número entre 0 e 10000: ")
b = input("Digite um número entre 0 e 10000: ")

lista1 = list(a)
lista2 = list(b)

print(lista1)
print(lista2)


lista3 = [] 
resto = 0

for x in range(len(lista1) -1 , -1, -1):

    if int (lista1[x]) + int (lista2[x]) + resto >= 10:
        lista3.append((int (lista1[x]) + int (lista2[x]) + resto) - 10)
        resto = 1

    else:
        print(int (lista1[x]) + int (lista2[x]) + resto)
        lista3.append(int (lista1[x]) + int (lista2[x]) + resto)
        resto = 0

print(lista3[::-1])

