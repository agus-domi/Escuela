palabra = input("Introduce una palabra: ")
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas
    return palabra == palabra[::-1]  # Comparar con su reverso
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")