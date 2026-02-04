# Ejercicio 19
# Python
# El Cajero Automático

# Inicializamos el saldo inicial (usamos un número para poder operar)
saldo = 100

while True:
    # Capturamos la entrada y la dividimos en una lista: ['D', '400']
    transaccion = input("Introduce la transaccion (D cantidad/ W cantidad): ").split()
    
    # Si el usuario pulsa Enter sin escribir nada, la lista está vacía y salimos
    if not transaccion:
        break
    
    # Extraemos la letra y la pasamos a minúscula para evitar errores
    operacion = transaccion[0].lower()
    
    # Convertimos el segundo elemento a float para permitir decimales (puntos)
    cantidad = float(transaccion[1])
    
    # Lógica del cajero: si es 'd' sumamos, si es 'w' restamos
    if operacion == "d":
        saldo = saldo + cantidad
    elif operacion == "w":
        saldo = saldo - cantidad
    else:
        # Por si el usuario escribe algo que no sea D o W
        print("Introduce datos validos")

# Una vez que el bucle termina con el break, mostramos el resultado final
print("---CUENTA BANCARIA---")
print(f"El total en tu cuenta es de: {saldo}")