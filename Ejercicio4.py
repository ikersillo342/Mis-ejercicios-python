#Ejercicio4
#python
#Pedir un numero entero positivo y validar la entrada, despues determinar si es primo y mostrar el mensaje
es_primo = True

while True:
    try:
        num = int(input("Dame un numero entero: "))
        if num >= 0:
            break  # Sale del bucle si es positivo
        else:
            print("El número no puede ser negativo")
    except ValueError:
        print("Por favor, introduce un número válido")

#Si el numero es 0 o 1, no se consideran primos
if num < 2:
    es_primo = False
else:
    #Probamos desde 2 hasta num-1
    for i in range(2, num):
        if num % i == 0: #Si el resto es 0, encontramos un divisor
            es_primo = False
            break #Finalizamos el for

#Mostramos el resultado
if es_primo:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")