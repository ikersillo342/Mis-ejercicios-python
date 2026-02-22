# Ejercicio 27
# Python
# Enunciado: Escribe un programa que acepte una secuencia de números separados por comas. 
# El programa debe elevar al cuadrado cada número que sea impar.

# Inicializamos las listas: una para todos los números y otra para los resultados
numeros_limpios = []
cuadrados = []

# Capturamos la entrada y .split(",") nos crea una lista de textos automáticamente
numeros = input("Dame los numeros que quieras: ").split(",")

for i in numeros:
    # Convertimos cada elemento de texto "i" a un número entero (int)
    valor_entero = int(i)
    # Guardamos el número en la lista general
    numeros_limpios.append(valor_entero)
    
    # Comprobamos si el número es impar usando el resto de la división (% 2)
    if valor_entero % 2 != 0:
        # Si es impar, calculamos su cuadrado y lo guardamos en una variable temporal
        resultados = valor_entero ** 2
        # Añadimos ese resultado a nuestra lista de cuadrados
        cuadrados.append(resultados)

# Convertimos cada número de 'cuadrados' a texto (str) para poder unirlos con comas
# El método .join() se encarga de que no aparezcan corchetes ni paréntesis en la salida
print(",".join(str(n) for n in cuadrados))
