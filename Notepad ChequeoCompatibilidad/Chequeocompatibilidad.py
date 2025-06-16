nombre1 = input("Ingrese el nombre de la primera persona: ")
nombre2 = input("Ingrese el nombre de la segunda persona: ")
letras = []
if len(nombre1) > len(nombre2):
    letras = list(nombre1.lower()) + list(nombre2.lower())
else:
    letras = list(nombre2.lower()) + list(nombre1.lower())
n = []
usadas = []
for letra in letras:
    if letra not in usadas:
        n.append(letras.count(letra))
        usadas.append(letra)

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
while len(n) > 2:
    n = compatibilidad(n)
print(n[0]*10+n[1])