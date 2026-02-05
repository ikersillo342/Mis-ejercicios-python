# Ejercicio 21
# Python
# Escribir un programa que acepte una secuencia de líneas (frases) y las imprima todas en mayúsculas.

# 1. Creamos una lista vacía que servirá como nuestro "almacén" de frases
lineas = []

# 2. Iniciamos un bucle infinito para pedir frases continuamente
while True:
    # Pedimos la frase y la convertimos a MAYÚSCULAS inmediatamente con .upper()
    frase = input("Dame la frase: ").upper()
    
    # Comprobamos si la frase está vacía (el usuario solo pulsó Enter)
    if not frase:
        # Si está vacía, rompemos el bucle para dejar de pedir datos
        break
    
    # 3. Verificamos si la frase NO está ya en nuestra lista (evitamos duplicados)
    elif frase not in lineas:
        # Si es una frase nueva, la añadimos al almacén
        lineas.append(frase)

# 4. Una vez fuera del bucle, recorremos la lista para mostrar los resultados
# 'frase' es una variable temporal que toma el valor de cada elemento en cada vuelta
for frase in lineas:
    print(frase)