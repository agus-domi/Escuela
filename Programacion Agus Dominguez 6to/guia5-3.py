# Ejercicio 3: Manipulación de listas
# Descripción: Este programa crea una lista de números aleatorios, muestra los primeros 5, el último elemento, intercambia el primero y el último, elimina el elemento del medio si la lista es impar, y muestra la lista sin el primer elemento.
import random
def lista_random(n):
    return [random.randint(0, 100) for _ in range(n)]
lista1=lista_random(10)
primeros=lista1[:5:]
ultimo=lista1[-1]
def intercambio(list):
    list[0], list[len(list)-1] = list[len(list)-1], list[0]
    return list
def eliminar_medio(list):
    if(len(list)%2!=0):
        list.pop(int(len(list)/2))
        return list
    else:
        return "La lista es par"
ultimos_sinuno=lista1[1::]
print(f"Lista: {lista1} \nPrimeros 5 : {primeros} \nUltimo: {ultimo}")
#print(f"Intercambio Primer y Ultimo: {intercambio(lista1)}")
#print(f"Lista con medio eliminado: {eliminar_medio(lista1)}")
#print(f"Lista sin el primero: {ultimos_sinuno}")