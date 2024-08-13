#Crear un juego en el que la computadora presente al jugador un problema matemático sencillo
# (suma, resta, multiplicación o división)
# y el jugador tenga que resolverlo.

import random

def adivinanza_matematica():
    operaciones = ["+", "-", "*", "/"]
    operacion = random.choice(operaciones)
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    
    
    if operacion == "/":
        numero1 = numero1 * numero2  # Aseguramos que la división sea exacta

    print("¡Bienvenido al juego de Adivinanza Matemática!")
    print(f"Resuelve el siguiente problema: {numero1} {operacion} {numero2}")
    
    if operacion == "+":
        respuesta_correcta = numero1 + numero2
    elif operacion == "-":
        respuesta_correcta = numero1 - numero2
    elif operacion == "*":
        respuesta_correcta = numero1 * numero2
    elif operacion == "/":
        respuesta_correcta = numero1 // numero2
    intentos = 3  # Número de oportunidades para adivinar

    while intentos > 0:
        try:
            respuesta = int(input("Introduce tu respuesta: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if respuesta == respuesta_correcta:
            print("¡Correcto! Has resuelto el problema.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Incorrecto. Te quedan {intentos} oportunidades.")
            else:
                print(f"Incorrecto. La respuesta correcta era {respuesta_correcta}.")    

    

adivinanza_matematica()
    
    
    
    

