#Cambio de divisas de quetzales a dollares y pesos mexicanos

divisas = {
    "USD": 0.13,
    "MXN": 2.31,
    "EURO": 0.12,
}

cantidad = int(input("Introduce cantidad de Quetzales: "))

simbolo = input("Introduce el simbolo de la divisa EURO, USD o MXN: ")
if simbolo not in divisas:
    print("Divisa no reconocible")
else:
    total = cantidad * divisas[simbolo]
    print(f"La conversion de {cantidad} quetzales a {simbolo} es {total:.2f} {simbolo} exactos.")

#By Ema322 