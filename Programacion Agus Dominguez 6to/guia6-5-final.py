matriz = [
    [3, 1, 8, 0, 0],
    [1, 4, 1, 0, 3],
    [0, 1, 0, 1, 6],
    [0, 0, 0, 0, 2]
]
fila = int(input("Ingrese la Fila "))
columna = int(input("Ingrese la Columna "))
suma = 0
if not columna-1 < 0:
    suma += matriz[fila][columna-1]
if not columna+1 >= len(matriz[0]):
    suma += matriz[fila][columna+1]
if not fila-1 < 0:
    suma += matriz[fila-1][columna]
if not fila+1 >= len(matriz):
    suma += matriz[fila+1][columna]
print(suma)