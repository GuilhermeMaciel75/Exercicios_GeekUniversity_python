lista = []
op = 1

for _ in range(5):
    n = float(input("Dige um número: "))
    lista.append(n)


while(op != 0):

    print("[1] - Vetor na ordem direta\n[2] - Vetor na ordem Inversa\n[0] - Sair")
    op = int(input())

    while(op != 1 and op != 0 and op != 2):
        op = int(input("Valor inválido, dige um entre 0, 1 ou 2"))

    if (op == 1):
        print(lista)

    elif(op == 2):
        print(lista[::-1])

