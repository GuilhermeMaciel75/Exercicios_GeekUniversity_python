import random

matriz5 = []

for i in range(5):
    coluna = []

    for j in range(5):
        while True:
            naoExiste = True
            valor = random.randint(0, 99)
            for k in range(0, i):
                if valor in matriz5[k]:
                    naoExiste = False
 
            if naoExiste:
                break
            else:
                continue
            
        coluna.append(valor)

    matriz5.append(coluna)

for x in range(len(matriz5)):
    print(matriz5[x])


