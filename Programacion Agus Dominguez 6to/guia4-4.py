# Ejercicio 4: Adivina el número
# Descripción: Este programa permite al usuario adivinar un número secreto entre 1000 y 9000, con un número ilimitado de intentos.
import random

def acierto_o_no(n, secreto):
    if n==secreto:
        return "acierto"
    elif n>secreto:
        return "mayor"
    elif n<secreto:
        return "menor"
    
rand=random.randint(1000,9000)
numero=int(input("ingrese un número: "))
while (numero<1000 or numero>9000):
    print("El numero debe estar entre 1000 y 9000")
    numero=int(input("ingrese otro número: "))
intentos=1
while acierto_o_no(numero,rand)!="acierto":
    print(acierto_o_no(numero,rand))
    numero=int(input("ingrese otro número: "))
    while (numero<1000 or numero>9000):
        print("El numero debe estar entre 1000 y 9000")
        numero=int(input("ingrese otro número: "))
    intentos+=1
if acierto_o_no(numero,rand)=="acierto":
    print(f"{acierto_o_no(numero,rand)} en {intentos} intentos")