# Ejercicio 15
# python
# Este programa genera una lista de edades y filtra quién puede entrar a un recinto.

import random  # Importamos la librería para generar números aleatorios

# Generamos la lista 'edades' usando random.sample.
# (range(0, 110)) es el rango de edades posibles.
# El número 20 le indica a Python que queremos exactamente 20 edades diferentes.
edades = random.sample(range(0, 110), 20)

# Creamos una lista vacía que servirá como nuestro "recinto" o "discoteca".
# Solo los que cumplan la condición entrarán aquí.
pueden_pasar = []

# Usamos un bucle for para examinar cada edad de la lista original una por una.
# En cada vuelta, la variable 'i' toma el valor de la edad actual.
for i in edades:
    # Verificamos la condición: ¿Es la edad actual mayor o igual a 18?
    if i >= 18:
        # Si se cumple, usamos .append(i) para añadir esa edad a la lista de admitidos.
        pueden_pasar.append(i)

# Mostramos por pantalla la lista final con todos los que han superado el filtro.
print(pueden_pasar)