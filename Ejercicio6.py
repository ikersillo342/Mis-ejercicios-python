# Ejercicio 6
# Python
# Pedir un numero entre 1 y 100, mostrar todos los numeros desde 1 hasta ese numero. Si es multiplo de 3 debe decir la palabra fizz, si es multiplo de 5 la palabra buzz y si es de...

while True: # Bucle infinito para validar que el usuario introduzca un dato correcto
    try:
        # Convertimos la entrada a entero para poder comparar el rango
        num = int(input("Dame un numero del 1 al 100: "))
        # Usamos 'and' para asegurar que el numero este estrictamente en el intervalo [1, 100]
        if num >= 1 and num <= 100:
            break # Si es correcto, rompemos el bucle while
        else:
            print("El numero introducido no es valido, por favor ingrese un numero valido:")
    except ValueError:
        # Atrapamos el error si el usuario introduce texto en lugar de numeros
        print("La entrada es incorrecta, por favor ingrese un numero entre 1 y 100:")

# Inicializamos contadores para las estadisticas finales
contador_diferente = 0 # Para los casos Fizz, Buzz y FizzBuzz
contador_normal = 0    # Para los numeros que no cambian

# Iniciamos el conteo. Usamos 'num + 1' para incluir el numero elegido por el usuario
for i in range(1, num + 1):
    
    # IMPORTANTE: Primero evaluamos si es multiplo de AMBOS (3 y 5)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        contador_diferente = contador_diferente + 1
    
    # Si no fue multiplo de ambos, miramos si es solo de 3
    elif i % 3 == 0:
        print("Fizz")
        contador_diferente = contador_diferente + 1
        
    # Si no, miramos si es solo de 5
    elif i % 5 == 0:
        print("Buzz")
        contador_diferente = contador_diferente + 1
        
    # Si no cumplio ninguna de las anteriores, es un numero normal
    else:
        print(f"{i}")
        contador_normal = contador_normal + 1

# Mostramos el resumen de la ejecucion
print(f"El total de numeros normales han sido: {contador_normal}")
print(f"El total de numeros cambiados es de: {contador_diferente}")     