# Ejercicio 12 (Basado en el Reto 16 de Practice Python)
# Python
# Generador de Contraseñas Aleatorias.

import random  # Importamos el módulo para generar selecciones al azar
import string  # Importamos el módulo que contiene grupos de caracteres (letras, símbolos...)

# Definimos nuestras fuentes de caracteres usando las constantes del módulo string
letras = string.ascii_letters  # Contiene todas las letras (a-z y A-Z)
numeros = string.digits        # Contiene los números del 0 al 9
simbolos = string.punctuation  # Contiene símbolos y signos de puntuación (!, @, #...)

# Juntamos todos los caracteres en una sola variable (nuestro "pool" de opciones)
todos = letras + numeros + simbolos

# Esta línea elige uno al azar pero no se guarda en ningún sitio (se podría borrar)
random.choice(todos)

# Inicializamos la variable donde guardaremos la contraseña como un texto vacío
password_final = ""

# Pedimos al usuario la longitud de la contraseña y la convertimos a número entero
password = int(input("Dime cuanto caracteres quieres que tenga la contraseña (Recomendado 8): "))

# El bucle 'for' se ejecutará tantas veces como el número que introdujo el usuario
for i in range(1, password + 1):
    # En cada vuelta, elegimos un carácter al azar de 'todos' y lo sumamos a la variable
    password_final = password_final + random.choice(todos)

# Una vez termina el bucle, mostramos el resultado final por pantalla
print(f"La contraseña final es: {password_final}")