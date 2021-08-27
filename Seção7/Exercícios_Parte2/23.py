import random

matriz1 = []

matriz3 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    coluna1 = []
    coluna2 = []

    for j in range(3):
        coluna1.append(random.randint(0, 20))
        

    matriz1.append(coluna1)
    

matriz2 = matriz1.copy()

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(f"{matriz3[i][j]} += {matriz1[i][k]} * {matriz2[k][j]}")
            matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
        
    
   


print("Matriz 1") 
for x in range(3):
    print(*matriz1[x])
            
print("Matriz 2")    
for y in range(3):
    print(*matriz2[y])

print("Matriz 3")    
for z in range(3):
    print(*matriz3[z])