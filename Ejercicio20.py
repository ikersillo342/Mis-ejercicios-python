# Ejercicio 20
# Python
#Escribir un programa que acepte una secuencia de palabras separadas por comas y las imprima ordenadas alfabéticamente, también separadas por comas.

# 1. Capturamos la entrada del usuario.
# Usamos .split(",") para convertir el texto en una LISTA de palabras.
# La coma dentro del paréntesis le dice a Python exactamente dónde debe "cortar".
frase = input("Dime una lista de palabras separadas por comas: ").split(",")

# 2. Aplicamos el método .sort() a la lista.
# Este método ordena los elementos de la lista alfabéticamente (A-Z) de forma automática.
frase.sort()

# 3. Mostramos el resultado final.
# Usamos ",".join(frase) para transformar la lista de nuevo en una sola cadena de texto.
# El "," al principio actúa como el "pegamento" que une cada palabra de la lista.
print(",".join(frase))