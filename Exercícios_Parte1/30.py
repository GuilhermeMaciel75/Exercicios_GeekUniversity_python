import random
conjunto1 = set({})
conjunto2 = set({})

for _ in range(10):
    conjunto1.add(random.randint(0, 100))
    conjunto2.add(random.randint(0, 100))

intersersao = conjunto1.intersection(conjunto2)
print(conjunto1)
print(conjunto2)
print(intersersao)

    
