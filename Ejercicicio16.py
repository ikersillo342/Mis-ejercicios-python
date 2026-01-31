# Ejercicio 16
# Python
# Lista de la compra

# Creamos la lista vacía donde se irán guardando los productos
lista_compra = []

# Iniciamos un bucle infinito para pedir productos hasta que el usuario decida parar
while True:
    # Pedimos el producto y lo convertimos a minúsculas para que 'PAN' y 'pan' sean lo mismo
    producto = input("¿Que quieres añadir a la lista? ").lower()
    
    # Si el usuario escribe "salir", rompemos el bucle inmediatamente
    if producto == "salir":
        break
    
    # Comprobamos si el producto NO está ya en nuestra lista para evitar duplicados
    if producto not in lista_compra:
        # Si es nuevo, lo añadimos al final de la lista
        lista_compra.append(producto)
    else:
        # Si ya existía, avisamos al usuario con un mensaje personalizado
        print(f"Oye, {producto} ya está en la lista.")

# Una vez fuera del bucle (cuando el usuario escribió "salir"), ordenamos alfabéticamente
lista_compra.sort()

# Finalmente, mostramos el resultado de la lista organizada por pantalla
print(lista_compra)