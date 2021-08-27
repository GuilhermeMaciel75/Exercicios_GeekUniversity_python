lista = []
impar = []

for _ in range(10):
    n = int(input("Dige um número: "))
    while(0 > n or n > 50):
        n = int(input("Valor Inválido, Dige outro número: "))
    
    lista.append(n)

for x in lista:

    if not(x % 2 == 0):
        impar.append(x)

for x in range(0, len(lista), 2):
    print(f"{lista[x]} {lista[x + 1]}")

for x in range(0, len(impar), 2):
        print(*impar[0:2])
        del impar[0:2]
        if not impar:
            break
