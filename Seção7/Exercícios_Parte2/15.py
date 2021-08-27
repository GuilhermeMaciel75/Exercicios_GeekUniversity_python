banco_de_notas = []

for i in range(2):
    coluna = []

    for j in range(10):
        n = input(f"Digite a questão {j + 1} do aluno {i + 1}: ")
        coluna.append(n)

    banco_de_notas.append(coluna)


gabarito = []
for q in range(10):
    gabarito.append(input(f"Digite o gabarito da questão {q + 1}: "))


resultado = {}
for aluno in range(2):

    nota = 0
    for questao in range(10):

        if banco_de_notas[aluno][questao] == gabarito[questao]:
            nota += 1
    resultado.update({aluno:nota})

print(resultado)
          
