banco_de_notas = []

for i in range(3):
    coluna = {}
    matriucula_aluno = input("Matrícula: ")
    coluna.update({'Mátricula':matriucula_aluno })

    for j in range(10):
        n = input(f"Digite a questão {j + 1} do aluno {i + 1}: ")
        coluna.update({str(j + 1): n})

    banco_de_notas.append(coluna)


print(banco_de_notas)


gabarito = []
for q in range(10):
    gabarito.append(input(f"Digite o gabarito da questão {q + 1}: "))

    
for aluno in range(1):

    nota = 0
    for questao in range(10):

        
        if banco_de_notas[aluno][str(questao + 1)] == gabarito[questao]:
            nota += 1

    banco_de_notas[aluno]['Nota'] = nota
    if nota >= 7:
        banco_de_notas[aluno]['Situação'] = 'Aprovado'
    
    else:
        banco_de_notas[aluno]['Situação'] = 'Reprovado'

print(banco_de_notas)