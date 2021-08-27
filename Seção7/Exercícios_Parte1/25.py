lista = []
i = 1

while (len(lista) < 100):

    if not(str(i)[-1] == '7' or i % 7 == 0):
        lista.append(i)
     
    i += 1
    
print(lista)

