# Ejercicio 2
# python
# Pide un numero entre 1 y 10 y muestra su tabla de multiplicar del 1 al 10.

# Pedimos el número y lo convertimos a entero para poder operar matemáticamente
numero = int(input("por favor ingresa un numero entre 1 y 10: "))

# Verificamos que el número esté realmente en el rango solicitado (1 al 10)
if 1 <= numero <= 10:
    
    # Iniciamos un bucle que irá del 1 al 10
    # Usamos 11 porque el límite superior de range nunca se incluye
    for i in range(1, 11):
        
        # Calculamos el producto de la multiplicación actual
        resultado = numero * i
        
        # Mostramos la línea de la tabla con un formato elegante
        # Ejemplo: "5 x 1 = 5"
        print(f"{numero} x {i} = {resultado}")
