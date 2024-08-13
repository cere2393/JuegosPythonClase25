from random import randint
def AdivinaElNumero():
    numerosecreto =randint(1,100)
    intentos=0
    
    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:

        intento= int(input("introduce tu numero"))
        intentos=intentos+1
        distancia=abs(numerosecreto-intento)

        if intento<numerosecreto:
            if distancia<=10:
                print("demasiado bajo y estas cerca, intenta de nuevo")
            else:
                print("demasiado bajo y estas lejos.intenta de nuevo")
        elif intento>numerosecreto:
            if distancia<=10:
                print("demasiado alto y estas cerca,intenta de nuevo")
            else:    
                print("demasiado alto y estas lejos intenta de nuevo")
        else:
            print(f"felicidades acertaste en {intentos}  intentos")    
            break

AdivinaElNumero()        