#Tabla de multiplicar
# Descripción: Este programa imprime la tabla de multiplicar del número ingresado por el usuario.
num = int(input("Ingrese el numero del que desea la tabla: "))
for i in range(1,11,1):
    print(f"{num} x {i} = {num*i}")