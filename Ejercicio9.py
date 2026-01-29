# Ejercicio 9
# Python
# Crear una lista vacía, llenarla con 3 nombres y buscar uno en ella.

# 1. Creamos el contenedor vacío
invitados = []

# 2. Llenamos la lista (Bucle de 3 vueltas)
for i in range(1, 3 + 1):
    # Usamos .lower() para que la búsqueda no falle por mayúsculas
    amigo = input("Dime a quien quieres añadir a la lista: ").lower()
    # .append() inserta el nombre al final de la 'fila'
    invitados.append(amigo)

# 3. Fase de consulta
buscar = input("¿A quien quieres buscar? ").lower()

# El operador 'in' verifica la existencia (devuelve True o False)
if buscar in invitados:
    # IMPORTANTE: Usamos 'buscar' para encontrar la posición correcta
    indice = invitados.index(buscar)
    # Recordatorio: Las listas empiezan en 0, así que el índice 1 es la 2ª posición
    print(f"¡Perfecto, {buscar} esta invitado! Esta en la posicion {indice}.")
else:
    print(f"Lo siento, {buscar} no esta en la lista. ")