def count_bits(n):
    numero_binario = bin(n)[2:]  # Convertir a binario y quitar el prefijo '0b'
    contar = 0
    for i in range(len(numero_binario)):
        if numero_binario[i] == '1':
            contar += 1
    return contar

# Programa para probar la función
def test_count_bits():
    casos_de_prueba = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 2),
        (1234, 5),
        (15, 4),
        (1023, 10),
    ]

    for entrada, esperado in casos_de_prueba:
        resultado = count_bits(entrada)
        print(f"count_bits({entrada}) = {resultado} (esperado: {esperado})")

test_count_bits()