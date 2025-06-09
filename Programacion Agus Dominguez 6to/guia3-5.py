# Ejercicio 5: Fibonacci
# Descripción: Este programa genera la secuencia de Fibonacci hasta el número ingresado por el usuario.
num=int(input("Ingrese la cantidad de numeros que desea ver: "))
numeros=[0,0]
for i in range(0, num, 1):
    suma=numeros[0]+numeros[1]
    print(suma)
    numeros[0]=numeros[1]
    numeros[1]=suma
    if(suma==0):
        numeros[1]=1