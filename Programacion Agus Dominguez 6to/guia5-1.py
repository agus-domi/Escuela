import random
def lista_random(n):
    return [random.randint(0, 100) for _ in range(n)]

def mejores_ventas(lista):
    ordenada=lista
    ordenada.sort(reverse=True)
    porcentaje = 0
    i=0
    while i < 3:
        porcentaje+=ordenada[i]
        i+=1
    return porcentaje*0.1
lista1 = lista_random(10)
print(mejores_ventas(lista1))