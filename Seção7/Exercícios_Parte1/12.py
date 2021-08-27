lista = []

for _ in range(5):
    n = int(input("Dige um número: "))
    lista.append(n)

print(f"O valor número da lista é {max(lista)} o menor é {min(lista)} e a média de todos os valores é {sum(lista)/len(lista)}")