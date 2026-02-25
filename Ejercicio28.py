# Ejercicio 28
# Python
# Escribe un programa que pida una palabra y diga si es un palíndromo o no (se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("Dame una palabra y te diré si es un palíndromo o no: ").lower()

rewind = palabra[::-1]

if palabra == rewind:
    print(f"Tu palabra es un palíndromo {palabra}  {rewind}")
else:
    print(f"Tu palabra no es un palíndromo {palabra} {rewind}")