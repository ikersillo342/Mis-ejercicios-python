# Ejercicio 26
# Python
# Enunciado: Aceptar una secuencia de datos (Nombre, Edad, Puntuación) 
# y ordenarlos por prioridad: 1º Nombre, 2º Edad y 3º Puntuación.

from operator import itemgetter

# Inicializamos la lista donde guardaremos los "packs" de alumnos
lista_datos = []

while True:
    # Capturamos la entrada del usuario
    datos = input("Dame tu nombre, tu edad y tu nota: ")
    
    # Si el usuario pulsa Enter sin escribir nada, salimos del bucle
    if not datos:
        break
    
    # Troceamos el texto por las comas para separar los tres valores
    datos_separados = datos.split(",")
    
    # Creamos una tupla con los datos y la añadimos a la lista.
    # Convertimos edad y nota a entero (int) para que la ordenación sea numérica.
    lista_datos.append((datos_separados[0], int(datos_separados[1]), int(datos_separados[2])))

# Ordenamos la lista usando múltiples niveles de prioridad (Nombre > Edad > Nota)
lista_datos.sort(key=itemgetter(0, 1, 2))

# Imprimimos los resultados de forma limpia recorriendo la lista
for alumno in lista_datos:
    # Accedemos a cada posición de la tupla: [0] es nombre, [1] es edad, [2] es nota
    print(alumno[0], "-", alumno[1], "años - Nota:", alumno[2])