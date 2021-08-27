n =  int(input("Digite o número de linhas do Triângulo de Pascal: "))

triangulo = []

for x in range(n):
    linha = []
    for y in range(x +1):
        if y == 0:
            linha.append(1)
        elif x == y:
            linha.append(1)
        else:
            linha.append(triangulo[x - 1][y - 1] + triangulo[x - 1][y])

    triangulo.append(linha)

for z in range(len(triangulo)):
    print(*triangulo[z])