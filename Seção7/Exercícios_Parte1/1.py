a = []

a.extend([1, 0, 5, -2, -5, 7])

soma = a[0] + a[1] + a[5]
print(soma)

a[3] = 1000

for x in a:
    print(x)