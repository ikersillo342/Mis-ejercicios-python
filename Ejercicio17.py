# Ejercicio 17
# Python
# La Agenda de Contactos

# Creamos un diccionario vacío para almacenar parejas de Nombre: Teléfono
agenda = { }

# Iniciamos el bucle principal del programa
while True:
    try:
        # Pedimos el nombre y lo normalizamos a minúsculas
        contacto = input("Dime el nombre de contacto que quieres agregar: ").lower()
        
        # Pedimos el teléfono (lo tratamos como texto para poder contar sus dígitos)
        telefono = input(f"Dime el telefono de {contacto}: ")
        
        # Validamos que el teléfono tenga exactamente 9 caracteres
        if len(telefono) == 9:
            print("¡Guardado con exito!")
            # Guardamos el teléfono en el diccionario usando el nombre como clave
            agenda[contacto] = telefono
        else:
            # Si no tiene 9 dígitos, avisamos al usuario y no lo guardamos
            print("El numero debe tener 9 digitos.")
            
        # Preguntamos si el usuario quiere continuar o cerrar la agenda
        # El .lower() con paréntesis es vital para que la comparación funcione
        salida = input("Si deseas salir escribe 'fin' ").lower()
        
        # Si la respuesta es exactamente "fin", rompemos el bucle
        if salida == "fin":
            break
            
    except ValueError:
        # Este bloque capturaría errores matemáticos o de conversión si usáramos int()
        print("Por favor, introduce un numero valido")

# --- Fase de consulta fuera del bucle ---

# Pedimos el nombre de la persona que queremos localizar
buscar = input("A quien quieres buscar? ").lower()

# Comprobamos si el nombre existe en las claves de nuestro diccionario
if buscar in agenda:
    # Si existe, mostramos el valor asociado (el teléfono)
    print(f"El telefono es: {agenda[buscar]} ")
else:
    # Si no está en la agenda, evitamos el error KeyError con este mensaje
    print("Ese contacto no existe.")