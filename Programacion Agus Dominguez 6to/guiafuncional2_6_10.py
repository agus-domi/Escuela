#6. Agregar signos de exclamación a las palabras
# Entrada: ["bien", "hecho"]
# Salida: ["¡bien!", "¡hecho!"]

def agregar_signos_exclamacion(palabra):
    return f"¡{palabra}!"
a = list(map(agregar_signos_exclamacion, ["bien", "hecho"]))
print(a)

#10. Evaluar si los números son pares (True/False)
# Entrada: [1, 2, 3, 4]
# Salida: [False, True, False, True]

def es_par(numero):
    return numero % 2 == 0
b = list(map(es_par, [1, 2, 3, 4]))
print(b)