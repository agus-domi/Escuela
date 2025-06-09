# Ejercicio 2: Sumar dos matrices
# Descripción: Este programa suma dos matrices de 2x3 y muestra el resultado.
import random
def matriz_random(n,m):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]
matriz1 = [[2,2,2], [2,2,2]]#matriz_random(4, 4)
matriz2 = [[1,1,1], [1,1,1]]#matriz_random(4, 4)
matriz3 = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
print(matriz1)
print(matriz2)
print(matriz3)