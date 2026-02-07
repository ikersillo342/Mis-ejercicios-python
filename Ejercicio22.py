# Ejercicio 22
# Python
# Escribir un programa que acepte una frase y cuente cuántas letras y cuántos dígitos (números) tiene.

# 1. Inicializamos el diccionario con los dos contadores en cero
# Usamos etiquetas (keys) claras para saber qué estamos contando
contador = {"LETRAS": 0, "DIGITOS": 0}

# 2. Pedimos al usuario que introduzca el texto
pedir = input("Dame una frase con letras y numeros: ")

# 3. Recorremos la frase carácter por carácter
for caracter in pedir:
    # Si el carácter actual es un número del 0 al 9
    if caracter.isdigit():
        # Sumamos 1 al valor asociado a la etiqueta "DIGITOS"
        contador["DIGITOS"] += 1
    # Si el carácter actual es una letra (a-z)
    elif caracter.isalpha():
        # Sumamos 1 al valor asociado a la etiqueta "LETRAS"
        contador["LETRAS"] += 1

# 4. Imprimimos los resultados finales accediendo al diccionario
print("LETRAS", contador["LETRAS"])
print("DIGITOS", contador["DIGITOS"])