# Ejercicio 13
# Python
# Tienes dos almacenes de datos (las listas a y b) y tu misión es encontrar qué objetos están guardados en ambos a la vez.

import random # Importamos el módulo para poder generar números aleatorios

# Generamos la lista 'a' con 10 números elegidos al azar entre el 1 y el 19
a = random.sample(range(1, 20), 10) 

# Generamos la lista 'b' con 12 números elegidos al azar entre el 1 y el 19
# Al ser tamaños distintos (10 y 12), probamos que el código es flexible
b = random.sample(range(1, 20), 12)

# Creamos una lista vacía llamada 'comunes' para ir guardando los números que coincidan
comunes = [ ]

# Empezamos un bucle para revisar la lista 'a' elemento por elemento
# En cada vuelta, el número actual se guarda en la variable 'i'
for i in a:
    # Preguntamos: ¿El número 'i' está en la lista 'b' Y ADEMÁS no lo hemos guardado ya en 'comunes'?
    # Esto último evita que si hay números repetidos, se guarden varias veces.
    if i in b and i not in comunes:
        # Si ambas condiciones se cumplen, añadimos el número a nuestra lista de resultados
        comunes.append(i)

# Una vez que el bucle termina de revisar toda la lista 'a', imprimimos el resultado final
print(comunes)