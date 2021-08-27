x = ""
c = 0
m = []
md = 0 # Maior na diagonal
mc = 0 # Maior em cima
mb = 0 # Maior em baixo
me = 0 # Maior na esquerda
mr = 0 # Maior na direita (right)

# formatação do arquivo matriz.txt

with open("matriz.txt", "r") as matrix:
	for line in matrix:
		m += [[]]
		for item in line:
			x += item
			if item == " ":
				x = ""
				pass
			elif item == "\n":
				x = ""
				pass
			elif len(x) == 2:
				m[c].append(x)
		c += 1

for i in range(m.count([])):
	m.remove([])

for a in range(len(m)):
	for b in range(len(m[a])):
		m[a][b] = int(m[a][b])

# formatação do arquivo matriz.txt

for a in range(len(m) - 3):
	for b in range(len(m[a]) - 3):
		foo = m[a][b] * m[a+1][b+1] * m[a+2][b+2] * m[a+3][b+3]
		if foo > md:
			md = foo
			
for a in range(len(m) - 3):
	for b in range(len(m[a])):
		foo = m[a+3][b] * m[a+2][b] * m[a+1][b] * m[a][b]
		if foo > mc:
			mc = foo

for a in range(len(m) - 3):
	for b in range(len(m[a])):
		foo = m[a][b] * m[a+1][b] * m[a+2][b] * m[a+3][b]
		if foo > mb:
			mb = foo

for a in range(len(m)):
	for b in range(0, len(m[a]), 4):
		foo = m[a][len(m[a]) - 1 - b] * m[a][len(m[a]) - 2 - b] * m[a][len(m[a]) - 3 - b] * m[a][len(m[a]) - 4 - b]
		if foo > me:
			me = foo

for a in range(len(m)):
	for b in range(len(m[a]) - 3):
		foo = m[a][b] * m[a][b+1] * m[a][b+2] * m[a][b+3]
		if foo > mr:
			mr = foo

valores = [md, mb, mc, me, mr]
nomes = ["Diagonal", "Baixo", "Cima", "Esquerda", "Direita"]
print(f"O maior produto de 4 numeros e na direção {nomes[valores.index(max(valores))]} com o valor {max(valores)}")