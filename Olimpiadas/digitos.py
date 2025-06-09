numero = int(input("Ingrese un número: "))
if numero < 0:
    numero = -numero
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1
print("El número de dígitos es:", digitos)