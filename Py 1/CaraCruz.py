
# Cara o cruz GAME

import random

opciones = ["cara", "cruz"]
usuario = input("Escribe cara o cruz: ").lower()

if usuario not in opciones:
    print("Error")
    quit()

resultado = random.choice(opciones)

print("El resultado es: ", resultado , "y tu elegiste" ,usuario)

if resultado == usuario:
    print("ganaste!")
else:
    print("perdiste")
