#Ejercicio 10
#Python
#Haz un piedra papel tinera para dos personas

Gana1 = 0
Gana2 = 0

while True:
        while True:
                 jugador1 = input("Jugador 1, Elige: Piedra, papel o tijera:").lower()
                 
                 if jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera":
                    break
                 else:
                     print("Jugador 1, introduce una respuesta valida")

        while True:             
                jugador2 = input("Jugador 2, Elige: Piedra, papel o tijeras:").lower()
                if jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijera":
                    break
                else:
                     print("Jugador 2, introduce una respuesta valida")
                
        if jugador1 == jugador2:
                print("EMPATE")

        elif jugador1 == "papel" and jugador2 == "piedra":
                print("¡Gana jugador 1! el papel gana a la piedra") 
                Gana1 = Gana1 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")

        elif jugador1 == "piedra" and jugador2 == "tijera":
                print("¡Gana jugador 1! la piedra gana a la tijera") 
                Gana1 = Gana1 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")
                      
        elif jugador1 == "tijera" and jugador2 == "papel":
                print("¡Gana jugador 1! la tijera gana al papel") 
                Gana1 = Gana1 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")
                        
        elif jugador2 == "papel" and jugador1 == "piedra":
                print("¡Gana el jugador 2! el papel gana a la piedra")
                Gana2 = Gana2 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")

        elif jugador2 == "piedra" and jugador1 == "tijera":
                print("¡Gana el jugador 2! la piedra gana a la tijera")
                Gana2 = + Gana2 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")

        elif jugador2 == "tijera" and jugador1 == "papel":
                print("¡Gana el jugador 2! la tijera gana al papel")
                Gana2 = + Gana2 + 1
                print(f"Resultado hasta ahora: {Gana1} - {Gana2}")
        
        continuar = input("¿Quieren jugar otra partida? (si/no): ").lower()
        if continuar == "no":
            print("--- RESUMEN FINAL ---")
            print(f"Jugador 1: {Gana1} victorias")
            print(f"Jugador 2: {Gana2} victorias")
            print("¡Hasta la próxima!")
            break    
