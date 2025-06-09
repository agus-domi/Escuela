#Adivina el número
# Descripción: Este programa permite al usuario adivinar un número secreto entre 1 y 9, con un máximo de 3 intentos.
import random
intentos = 0
secreto = random.randint(1,9)
while (intentos<3):
    num = int(input("Ingrese un numero entre 1 y 9: "))
    if num == secreto:
        print("Ganaste!")
        break
    elif intentos==2:
        print("Perdiste")
    intentos += 1