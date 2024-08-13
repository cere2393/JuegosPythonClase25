
import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        distancia=abs(numero_secreto - intento) 
        #if intento < numero_secreto:
            #print("Demasiado bajo, intenta de nuevo.")
        if distancia <= 10:
            print("¡Muy cerca!")
            
        #elif intento > numero_secreto:
            #print("Demasiado alto, intenta de nuevo.")
        elif distancia > 10:
            print("¡Muy lejos!")
        elif intento==numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()


