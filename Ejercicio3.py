# Ejercicio3
# python
# pedir al usuario numero N y calcular todos los numeros pares desde 2 hasta N

# Inicializamos el acumulador 'suma' en 0 para ir guardando el total
suma = 0

# Pedimos el límite al usuario y lo convertimos a un número entero
N = int(input("Por favor ingresa un numero N: "))

# Iniciamos el bucle for
# Empieza en 2, llega hasta N (por eso el N + 1) y salta de 2 en 2
for i in range(2, N + 1, 2):
    
    # En cada vuelta, sumamos el valor actual de 'i' a nuestra variable 'suma'
    suma += i

# Al terminar el bucle, mostramos el resultado final usando f-strings
print(f"La suma de todos los numeros pares desde 2 hasta {N} es: {suma}")