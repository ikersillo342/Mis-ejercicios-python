# Ejercicio 24
# Python
# Escribir un programa que calcule el valor de $a + aa + aaa + aaaa$ partiendo de un solo dígito dado por el usuario.

# 1. Pedimos la entrada al usuario. 
# Importante: La dejamos como texto (string) para poder "pegar" los caracteres después.
num = input("Dame un numero: ")

# 2. Creamos las versiones concatenadas y las convertimos a número (int).
# num1: Es el número individual (ej: 9)
num1 = int(num)

# num2: Pegamos el texto dos veces (ej: "9"+"9" = "99") y luego lo hacemos entero.
num2 = int(num + num)

# num3: Pegamos el texto tres veces (ej: "999") y lo hacemos entero.
num3 = int(num + num + num)

# num4: Pegamos el texto cuatro veces (ej: "9999") y lo hacemos entero.
num4 = int(num + num + num + num)

# 3. Sumamos todos los valores. 
# Como todos son ahora de tipo 'int', Python realizará una suma matemática real.
resultado = num1 + num2 + num3 + num4

# 4. Mostramos el total en la terminal.
print(resultado)