# Ejercicio 29
# Python
# Escribe un programa que cuente la frecuencia de las palabras de una frase. El resultado debe imprimirse después de ordenar las palabras alfabéticamente.

import string # Importamos la librería para manejar signos de puntuación automáticamente

frecuencia = {}

# 1. Normalizamos la entrada: .lower() para ignorar mayúsculas y .split() para separar palabras
frase = input("Dime varias palabras: ").lower().split()

for p in frase:
    # 2. Limpieza profunda: .strip(string.punctuation) elimina comas, puntos, etc., de los extremos
    palabra_limpia = p.strip(string.punctuation)
    
    # 3. Solo procesamos si la palabra no ha quedado vacía (por si el usuario puso solo un signo)
    if palabra_limpia:
        # 4. Método .get(): si la palabra no existe devuelve 0, si existe devuelve su cuenta actual.
        # En ambos casos le sumamos 1 y actualizamos el diccionario.
        frecuencia[palabra_limpia] = frecuencia.get(palabra_limpia, 0) + 1

# 5. EL RANKING: Ordenamos las palabras (claves del diccionario).
# key = frecuencia.get -> Ordena basándose en los números (valores), no en las letras.
# reverse = True -> Hace que el orden sea descendente (de la que más sale a la que menos).
for p in sorted(frecuencia, key = frecuencia.get, reverse=True):
    # 6. Imprimimos cada palabra con su frecuencia usando una f-string
    print(f"{p}:{frecuencia[p]}")