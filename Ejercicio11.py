#Ejercicio 11
#Python
#La maquina debe poner un numero al azar y el usuario debe adivinarlo.

intentos = 0

import random
aleatorio = random.randint(1,9)

while True:
    respuesta = input("Elige un numero del 1 al 9 o pon exit para salir ").lower()

    if respuesta == "exit" or respuesta == "Exit" or respuesta == "EXIT":
        print(f"Te rindes... el número era {aleatorio}. Hiciste {intentos} intentos")
        break
    try:
        numero = int(respuesta)

        if numero == aleatorio:
            print("¡Has ganado!")
            intentos = intentos + 1
            break
        elif numero < aleatorio:
            print("Demasiado bajo")
            intentos = intentos + 1
        elif numero > aleatorio:
            print("Demasiado alto")
            intentos = intentos + 1
    except ValueError:
        print("¡ERROR! Por favor, introduce un numero valido o 'exit'")

print(f"¡Lo lograste! te ha llevado {intentos} intentos")