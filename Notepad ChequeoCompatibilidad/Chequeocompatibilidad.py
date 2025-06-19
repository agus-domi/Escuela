#Este programa calcula la compatibilidad entre dos personas basándose en sus nombres.
#Entrada de Datos y preparación de Letras
nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")
letras = []
if len(nombre1) > len(nombre2):
    letras = list(nombre1.lower()) + list(nombre2.lower())
else:
    letras = list(nombre2.lower()) + list(nombre1.lower())
#Conteo de Letras Unicas
cant_letras = []
usadas = []
for letra in letras:
    if letra not in usadas:
        cant_letras.append(letras.count(letra))
        usadas.append(letra)
#Función de Compatibilidad(Reducir la lista de números)
def compatibilidad(numeros):
    mitad = len(numeros) // 2 - 1
    if len(numeros) % 2 == 0:
        i = 0
        while i <= mitad:
            numeros [i] = numeros[i] + numeros[-(i + 1)]
            i += 1
    else:
        i = 0
        while i < mitad + 1:
            numeros[i] = numeros[i] + numeros[-(i + 1)]
            i += 1
    return numeros[:mitad + 1] if len(numeros) % 2 == 0 else numeros[:mitad + 2]
#n = [1,1,1,1,1,1,1,1,1]
# 2, 2, 2, 2, 1
# 3, 4, 2
# 5, 4
#Proceso Principal
# Mientras la lista de números tenga más de 2 elementos, se aplica la función de compatibilidad.
while len(cant_letras) > 2:
    cant_letras = compatibilidad(cant_letras)
    if len(cant_letras) == 2 and cant_letras[0] >= 10:
        cant_letras.append(cant_letras[1])
        cant_letras[1] = cant_letras[0] % 10
        cant_letras[0] = cant_letras[0] // 10
    elif len(cant_letras) == 2 and cant_letras[1] >= 10:
        cant_letras.append(cant_letras[1] % 10)
        cant_letras[1] = cant_letras[1] // 10
#Resultado Final
compatibilidad_final = cant_letras[0] * 10 + cant_letras[1]
print(f"La compatibilidad entre {nombre1} y {nombre2} es de {compatibilidad_final}%")