lista = []

for _ in range(10):
    n = int(input("Digite um valor: "))
    while(n in lista):
        n = int(input("Valor já contido na lista, digite um outro valor: "))
    
    lista.append(n)

print(lista)