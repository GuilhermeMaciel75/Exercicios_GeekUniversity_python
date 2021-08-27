'''
Resolução utilizanado Listas

nome = []
idade = []


for x in range(3):
    nome.append(input("Digite o nome do Aluno: "))
    idade.append(float(input("Digite a altura do Aluno: ")))


print(f"O Maior aluno possui {max(idade)}m e o seu número é {idade.index(max(idade)) + 1}")
print(f"O Menor aluno possui {min(idade)}m e o seu número é {idade.index(min(idade)) + 1}")
'''

dicio = {}

for x in range(3):
    nome = (input("Digite o nome do Aluno: "))
    altura = (float(input("Digite a altura do Aluno: ")))
    dicio.update({nome:altura})

for chave, valor in dicio.items():

    if valor == min(dicio.values()):
        print(f"O Maior aluno possui {valor:.2f}m e o seu número é {chave}")

    elif valor == max(dicio.values()):
        print(f"O Menor aluno possui {valor:.2f}m e o seu número é {chave}")