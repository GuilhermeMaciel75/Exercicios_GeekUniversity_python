
matriz10 = []

for i in range(10):
    coluna = []

    for j in range(10):
        
        if i < j:
            conta = 2 * i + 7 * j - 2
            coluna.append(conta)

        elif i == j:
            conta1 = (3 * i * i) - 1 
            coluna.append(conta1)

        elif i > j:
            conta2 = (4 *(i ** 3)) - (5 * (j ** 2)) + 1
            coluna.append(conta2)

    matriz10.append(coluna)

for x in range(len(matriz10)):
    print(matriz10[x])


