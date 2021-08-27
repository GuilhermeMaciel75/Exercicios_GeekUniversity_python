notas = []

for x in range(15):
    n = float(input(f"Dige a nota do aluno {x + 1}: "))
    notas.append(n)

media = sum(notas)/len(notas)

print("A média dos 15 alunos é: {:.2f}".format(media))