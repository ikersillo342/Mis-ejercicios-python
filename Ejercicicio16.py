# Ejercicio 16
# Python
# Lista de la compra

lista_compra = [ ]

while True:
   producto = input("¿Que quieres añadir a la lista? ").lower()
   if producto == "salir":
      break
   
   if producto not in lista_compra:
         lista_compra.append(producto)
   else:
       print(f"Oye, {producto} ya está en la lista.")

lista_compra.sort()

print(lista_compra)