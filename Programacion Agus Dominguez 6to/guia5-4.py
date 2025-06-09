## Ejercicio 4: Palíndromo
# Escribir un programa que determine si una palabra es un palíndromo.
def palindromo(palabra):
    if palabra[::-1] == palabra:
        return True
    else:
        return False
a="avion"
b="oso"
print(palindromo(a))
print(palindromo(b))