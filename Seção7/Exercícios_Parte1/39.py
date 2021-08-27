x = int(input('Digite o números de linhas do triangulo: '))
lista = list()
lista1 = list()
for c in range(0, x):
    for c1 in range(0, c + 1):
        if c1 == 0:
            s = 1
            lista1.append(s)
        elif c1 == c:
            s = 1
            lista1.append(s)
        else:
            s = lista[c - 1][c1- 1] + lista[c-1][c1]
            lista1.append(s)
    lista.append(lista1[:])
    lista1.clear()


print(lista)

for n in lista:
    for n1 in n:
        print(n1, end=' ')
    print(end='\n')

