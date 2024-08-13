
#Crear una versión simple del juego "Ahorcado" donde el jugador intente adivinar una palabra letra por letra.
import random

def ahorcado():
    # Lista de palabras con pistas asociadas
    palabras_y_pistas = [("python", "Es un lenguaje de programación ."), ("programacion", "para escribir código."),
    ("ahorcado", " el nombre de este juego."),("desarrollo", "Proceso de creación de software."),
    ("juego", "actividad de entretenimiento.")]
    
    palabra_secreta, pista = random.choice(palabras_y_pistas)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Pista: {pista}")
    print("_ " * len(palabra_secreta))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(palabra_mostrada))

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break
    else:
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'.")

ahorcado()
