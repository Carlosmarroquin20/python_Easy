import random

def ruleta_rusa():
    # La ruleta tiene 6 chambers
    chambers = [0, 0, 0, 0, 0, 1]  # 1 representa la bala
    random.shuffle(chambers)  # Mezclar las chambers

    # Elige una chamber al azar
    chamber_seleccionada = random.choice(chambers)

    # Simula disparar la ruleta
    if chamber_seleccionada == 1:
        print("¡Bang! Perdiste.")
    else:
        print("¡Click! Te salvaste.")

# Ejecutar el juego
ruleta_rusa()
