# Ejercicio 7
# Python
# Pedir dos numeros enteros "Inicio" y "Fin", validar que inicio sea menor que fin, 
# recorrer todos los numeros entre ellos inclusive y contar los impares y sumar mult de 4

while True:
    try:
        # Pedimos los dos límites del rango
        start = int(input("Dime el primer numero(Inicio):"))
        end = int(input("Dime el segundo numero(Fin):"))
        
        # Validación lógica: el inicio debe ser menor al fin
        if start < end:
            break
        else:
            # Si el usuario se equivoca, le damos una pista usando f-string
            print(f"Datos incorrectos, por favor empiece con un numero menor que {end}")
    except ValueError:
        print("Datos incorrectos por favor escriba un numero de inicio y otro de final")

# Inicializamos el contador y el acumulador
numeros_impares = 0
suma_total = 0

# El range con + 1 para que incluya el último número (el límite 'end')
for i in range(start, end + 1):
    
    # Filtro 1: ¿Es impar? (Si el resto de dividir por 2 es distinto de 0)
    if i % 2 != 0:
        numeros_impares = numeros_impares + 1
    
    # Filtro 2: ¿Es múltiplo de 4? (Si el resto de dividir por 4 es 0)
    # Usaste elif porque un número no puede ser impar y múltiplo de 4 al mismo tiempo. ¡Eficiente!
    elif i % 4 == 0:
        suma_total = suma_total + i

# Resultados finales
print(f"El total de numeros impares es: {numeros_impares}")
print(f"La suma total de los multiplos de 4 es de: {suma_total}")