# Ejercicio 1
# python
# Saludo personalizado, pide el nombre, edad y muestra el mensaje: Hola {nombre}, tienes {edad} años. 
# Y si tiene menos de 18 años mostrar eres menor de edad.

#Pedimos el nombre al usuario (input siempre guarda texto por defecto)
nombre = input("por favor ingresa tu nombre: ")

#Pedimos la edad y la convertimos a entero (int) para poder compararla después
edad = int(input("por favor ingresa tu edad: "))

#Imprimimos el saludo usando una f-string para insertar las variables
print(f"Hola {nombre}, tienes {edad} años.")

#Estructura condicional para verificar si es menor de edad
if edad < 18:
    #Esta línea solo se ejecuta si la condición (edad < 18) es verdadera
    print("eres menor de edad.")