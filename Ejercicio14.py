# Ejercicio 14
# python
# Generador de nombres de usuario

import random  # Importamos para elegir elementos al azar
import string  # Importamos para acceder a grupos de caracteres como números

# Definimos nuestras fuentes de datos
numeros = string.digits  # Contiene los dígitos del '0' al '9'
adjetivos = ["pro", "shadow", "master", "plus", "god", "wizard"] # Lista de palabras clave

# Selección aleatoria: aquí elegimos una sola pieza de cada saco
adj_alazar = random.choice(adjetivos) # Escoge un adjetivo al azar de la lista
num_alazar = random.choice(numeros)   # Escoge un número al azar de la cadena de dígitos

# Entrada de datos del usuario
nombre = input("Dime tu nombre: ").lower()     # Convertimos a minúsculas para que quede mejor
anyo = int(input("Dime tu año de nacimiento: ")) # Pedimos el año como número entero
primera_letra = nombre[0]                      # "Slicing": extraemos solo el primer carácter

# Construcción de las sugerencias usando f-strings
opcion_1 = f"{nombre}{anyo}"                    # Combinación simple: nombre + año
opcion_2 = f"{adj_alazar}{nombre}"              # Combinación estilo gamer: adjetivo + nombre
opcion_3 = f"{primera_letra}_{anyo}_{num_alazar}" # Combinación compleja con guiones y azar

# Salida de resultados por pantalla
print("---Estas son las opciones---")
print(f"{opcion_1}")
print(f"{opcion_2}")
print(f"{opcion_3}")