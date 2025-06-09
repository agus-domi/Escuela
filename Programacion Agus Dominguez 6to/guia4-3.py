# Ejercicio 3: Escribir una función que reciba un número del 1 al 10 y retorne la nota correspondiente según la siguiente tabla:
def nota(num):
    if num==10:
        return "A"
    elif num==9:
        return "B"
    elif num==8:
        return "C"
    elif num==7:
        return "D"
    elif num==6:
        return "E"
    else:
        return "F"
print(nota(10))
print(nota(9))
print(nota(8))
print(nota(7))
print(nota(6))
print(nota(5))
print(nota(4))