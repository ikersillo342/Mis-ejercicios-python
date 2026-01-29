# Ejercicio 8
# Python
# Pide el nombre de un producto(str), pide el precio(float), pide la cantidad(int), y pregunta el usuario si tiene un cupon de descuento(bool). Calcula el subtotal

# --- Catálogo visual para el usuario ---
print("---LISTA DE PRODUCTOS---")
print("Tornillos: 1ªud/0.50")
print("Martillos: 1ª/1.50")
print("Destornilladores: 1ª/1.65")

# --- Base de datos del sistema ---
# Usamos listas paralelas: la posición en 'productos' coincide con su valor en 'precios'
productos = ["tornillo", "martillo", "destornillador"]
precios = [0.50, 1.50, 1.65]

# --- Inicialización de variables de estado ---
Subtotal = 0
Vip = False
tiene_descuento = False

# --- Bucle de validación de producto ---
# No dejamos avanzar al programa hasta que el usuario elija un producto existente
while True:
    # Convertimos la entrada a minúsculas con .lower() para evitar errores de coincidencia
    producto = input("Introduce el nombre del producto por favor: ").lower()
    
    if producto in productos:
        # Si el producto existe, localizamos su índice para obtener el precio correcto
        indice = productos.index(producto)
        precio_unidad = precios[indice]
        print(f"Has elegido {producto}, cuesta {precio_unidad}€")
        break  # Rompemos el bucle infinito al tener un dato válido
    else:
        # Feedback de error si el producto no está en la lista
        print(f"Lo sentimos, '{producto}' no está en nuestro inventario. Inténtelo de nuevo.")
        print("Productos disponibles: tornillo, martillo, destornillador")

# --- Recogida de datos de compra ---
cantidad = int(input("Dime la cantidad que quieres de ese producto:"))
cliente = str(input("Eres socio Vip?")).lower()

# --- Cálculos matemáticos iniciales ---
Subtotal = cantidad * precio_unidad
# Esta variable guarda el valor del ahorro potencial (5%)
subtotal_condescuento = Subtotal * 0.05

# --- Lógica de negocio (Descuentos y Condiciones) ---
# Caso 1: Es VIP y cumple el gasto mínimo para descuento
if cliente == "si" and Subtotal >= 20:
    Vip = True
    tiene_descuento = True
    # Aplicamos la resta del ahorro al subtotal original
    total_final = Subtotal - (Subtotal * 0.05)
    print("Se ha aplicado un 5% de descuento VIP.")

# Caso 2: Es VIP pero no gasta lo suficiente para la oferta
elif cliente == "si" and Subtotal < 20:
    Vip = True
    tiene_descuento = False
    total_final = Subtotal
    print("Eres VIP, pero necesitas gastar más de 20€ para el descuento.")

# Caso 3: No es VIP o el texto introducido no es "si"
else:
    Vip = False
    tiene_descuento = False
    total_final = Subtotal

# --- Salida de información formateada ---
# Usamos :.2f para mostrar siempre dos decimales, como en una factura real
print(f"El precio total del producto es de: {total_final:.2f}€")
