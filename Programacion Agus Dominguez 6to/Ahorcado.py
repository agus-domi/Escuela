import os
import random

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar():
    palabras = ["pizza", "hamburguesa", "pasta", "ensalada", "sushi", "tacos", "burrito", "lasagna", "paella", "ceviche", "milanesa", "empanadas", "asado", "locro", "ñoquis"]

    palabra_secreta = random.choice(palabras)
    vidas = 6
    letras_adivinadas = []
    pista = ['_' for _ in palabra_secreta]

    while vidas > 0 and '_' in pista:
        print("\nPalabra:", ' '.join(pista))
        print("Vidas restantes:", vidas)
        letra = input("Adivina una letra: ").lower()
        limpiar_pantalla()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    pista[i] = letra
            print("¡Bien! La letra está en la palabra.")
        else:
            vidas -= 1
            print("Incorrecto. Esa letra no está en la palabra.")

    if '_' not in pista:
        print("\n¡Felicitaciones! Adivinaste la palabra:", palabra_secreta)
    else:
        print("\nPerdiste. La palabra era:", palabra_secreta)

# Bucle principal
while True:
    limpiar_pantalla()
    jugar()
    respuesta = input("\n¿Querés jugar otra vez? (s/n): ").lower()
    if respuesta != 's':
        print("¡Gracias por jugar! Hasta la próxima.")
        break
