# Ejercicio 18
# Python
# TPV de la fruteria

# Definimos un diccionario con precios (Floats/Decimales)
# Aquí no hay inputs, los datos ya viven en el código
precios = {
    "manzana": 1.50,
    "pera": 1.80,
    "aguacate": 2.00,
}

# Cantidades fijas (Integers/Enteros)
cant_manzanas = 4
cant_peras = 2
can_aguacates = 3 # Ojo, aquí tienes una pequeña errata en el nombre (can vs cant), ¡pero funciona!

# Operaciones matemáticas directas
# Python sabe que son números, así que multiplica sin rechistar
total_manzana = 1.50 * cant_manzanas
total_pera = 1.80 * cant_peras

# Sumamos los subtotales para obtener el total de la cuenta
subtotal = total_manzana + total_pera

# Mostramos el resultado usando una f-string
# f"{subtotal}" mete el valor del número directamente en el texto
print(f"El total de los productos es de: {subtotal}")