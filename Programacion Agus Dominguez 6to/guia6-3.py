# Ejercicio 3: Contar la cantidad de veces que aparece el número 9 en una matriz.
# Descripción: Este programa cuenta cuántas veces aparece el número 9 en una matriz de enteros.
import random
def matriz_random(n,m):
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]
cant_9 = 0
matriz1 = [[9,9,2], [2,2,2]]#matriz_random(4, 4)
for i in range(len(matriz1)):
    cant_9 += matriz1[i].count(9)
print(cant_9)