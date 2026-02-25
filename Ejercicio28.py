# Ejercicio 28
# Python
# Escribe un programa que pida una palabra y diga si es un palíndromo o no (se lee igual de izquierda a derecha que de derecha a izquierda).

# 1. Solicitamos la entrada del usuario
palabra = input("Dame una palabra y te diré si es un palíndromo o no: ")

# 2. Invertimos la palabra usando 'slicing' de Python
# La sintaxis [::-1] crea una copia del string leída desde el final hacia el principio
rewind = palabra[::-1]

# 3. Comparamos la palabra original con la invertida
if palabra == rewind:
    # Si son idénticas, es un palíndromo
    print(f"Tu palabra es un palíndromo {palabra}  {rewind}")
else:
    # Si son diferentes, no lo es
    print(f"Tu palabra no es un palíndromo {palabra} {rewind}")