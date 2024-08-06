#Piedra papel o tijera en py

import random

opciones = ["tijera", "papel", "piedra"]

usuario = input("Elige... ").lower()
pc = random.choice(opciones)

if usuario not in opciones:
    print("Error ya que no elegiste bien!")
    quit()

if usuario == pc:
    print(f"Empate, ya que la pc eligio: {pc} y tu {usuario}")
elif usuario == "piedra" and pc == "papel" or usuario == "papel" and pc == "tijera" or usuario == "tijera" and pc == "pieda":
    print(f"Perdiste!! , ya que la pc eligio: {pc} y tu {usuario}")
else:
    print(f"Ganaste!!, ya que la pc eligio: {pc} y tu {usuario}")