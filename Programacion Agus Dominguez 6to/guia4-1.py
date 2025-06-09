## Ejercicio 1: Factorial de un número
# Descripción: Este programa calcula el factorial de un número ingresado por el usuario.
def factorial(num):
    for i in range(4,1, -1):
        num=num*i
    return num
print(factorial(5))