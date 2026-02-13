## Ejercicio 25
# Python
# Comprobar si una contraseña es segura.

# 1. Pedimos las contraseñas y las convertimos en una lista usando la coma como separador
user_passw = input("Dame una varias contraseñas separadas por comas: ").split(",")

# 2. Creamos la lista vacía donde iremos guardando solo las que cumplan los requisitos
validas = [ ]

# 3. BUCLE EXTERIOR: Recorremos cada contraseña de la lista que creó el .split()
for password in user_passw:
    # Limpiamos posibles espacios en blanco alrededor de la contraseña
    password = password.strip()

    # Sensores de seguridad: los reiniciamos a False para cada nueva contraseña
    tiene_mayus = False
    tiene_minus = False
    tiene_num = False
    tiene_simbolo = False

    # 4. BUCLE INTERIOR: Analizamos cada letra/carácter de la contraseña actual
    for letra in password:
        if letra.isupper():
            tiene_mayus = True
        elif letra.islower():
            tiene_minus = True
        elif letra.isdigit():
            tiene_num = True
        # Comprobamos si el carácter actual es uno de los símbolos permitidos
        elif letra in "$#@":
            tiene_simbolo = True
            
    # 5. VALIDACIÓN: Tras revisar todas las letras, comprobamos si cumple TODO
    # (Longitud entre 6 y 12 Y todos los sensores en True)
    if (len(password) >= 6 and len(password) <= 12 and 
        tiene_mayus and tiene_minus and tiene_num and tiene_simbolo):
        
        # Si pasa la prueba, la guardamos en nuestra lista de aprobadas
        validas.append(password)

# 6. RESULTADO FINAL: Unimos las contraseñas válidas con comas para mostrarlas
print(",".join(validas))