# Ejercicio 23
# Python
# Escribir un programa que acepte una frase y calcule el número de letras mayúsculas y letras minúsculas.

contador = {"MAYUSCULAS": 0, "MINUSCULAS": 0}

pedir = input("Dame una frase con MAYUSCULAS y minusculas: ")

for caracter in pedir:
    if caracter.isupper():
        contador["MAYUSCULAS"] += 1
    elif caracter.islower():
        contador["MINUSCULAS"] += 1

print("MAYUSCULAS", contador["MAYUSCULAS"])
print("MINUSCULAS", contador["MINUSCULAS"])
