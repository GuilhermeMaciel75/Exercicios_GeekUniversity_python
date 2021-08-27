import random

matriz1 = []
matriz2 = []
matriz3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    coluna1 = []
    coluna2 = []

    for j in range(4):
        coluna1.append(random.randint(0, 100))
        coluna2.append(random.randint(0, 100))

    matriz1.append(coluna1)
    matriz2.append(coluna2)


for i in range(4):
    for j in range(4):

        if matriz1[i][j] >= matriz2[i][j]:
            matriz3[i][j] = matriz1[i][j]

        else:
            matriz3[i][j] = matriz2[i][j]

print("Matriz 1") 
for x in range(4):
    print(matriz1[x])
            
print("Matriz 2")    
for y in range(4):
    print(matriz2[y])

print("Matriz 3")    
for z in range(4):
    print(*matriz3[z])