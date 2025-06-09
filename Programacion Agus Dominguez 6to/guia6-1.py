import random
def matriz_random(n,m):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]
matriz1 = matriz_random(4, 4)
print(matriz1)
for i in range(len(matriz1)):
    print(matriz1[i][i])