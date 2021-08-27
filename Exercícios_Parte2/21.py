import random

matriz1 = []
matriz2 = []
matriz3 = [[0,0],[0,0]]

for i in range(2):
    coluna1 = []
    coluna2 = []

    for j in range(2):
        coluna1.append(random.randint(0, 100))
        coluna2.append(random.randint(0, 100))

    matriz1.append(coluna1)
    matriz2.append(coluna2)

print("Matriz 1") 
for x in range(2):
    print(matriz1[x])
            
print("Matriz 2")    
for y in range(2):
    print(matriz2[y])


op = 0
while(op != 5):
    op = int(input("\n[1] - Somar as duas Matrizes\n[2] - Subtrair a primeira e a Segunda matriz\
    \n[3] - Adicionar a constante às duas Matrizes\n[4] - Imprimir as Matrizes\n"))

    if op == 1:
        for i in range(2):
            for j in range(2):
                matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
        
        print("Op realizada")

    elif op == 2:
        for i in range(2):
            for j in range(2):
                matriz3[i][j] = matriz1[i][j] - matriz2[i][j]

    elif op == 3:
        constante = int(input("Digite o valor da constante"))
        for i in range(2):
            for j in range(2):
                matriz1[i][j] = matriz1[i][j] + constante
                matriz2[i][j] = matriz2[i][j] + constante
    
    elif op == 4:

        print("Matriz 1") 
        for x in range(len(matriz1)):
            print(matriz1[x])
            
        print("Matriz 2")    
        for y in range(len(matriz2)):
            print(matriz2[y])


        print("Matriz 3")
        for z in range(len(matriz3)):
            print(matriz3[z])