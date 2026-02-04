#Ejercicio 19
#Python
#El Cajero Automático

saldo = 100

while True:
    transaccion = input("Introduce la transaccion (D cantidad/ W cantidad): ").split()    
    if not transaccion:
        break
    operacion = transaccion[0].lower()
    cantidad = float(transaccion[1])

    if operacion == "d":
        saldo = saldo + cantidad
    elif operacion == "w":
        saldo = saldo - cantidad
    else:
        print("Introduce datos validos")

print("---CUENTA BANCARIA---")
print(f"El total en tu cuenta es de: {saldo}")