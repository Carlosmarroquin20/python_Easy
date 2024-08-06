import random

def revolver_palabras(frase):
    palabras = frase.split()
    random.shuffle(palabras)
    return ' '.join(palabras)

def main():
    # Solicita al usuario que ingrese una frase
    frase_original = input("Escribe una frase: ")
    
    # Revuelve las palabras de la frase
    frase_revolvida = revolver_palabras(frase_original)
    
    # Muestra la frase con las palabras revueltas
    print(f"Frase con palabras revueltas: {frase_revolvida}")
    
    # Pregunta al usuario si quiere ver la frase original
    ver_original = input("¿Quieres ver la frase original? (sí/no): ").strip().lower()
    
    if ver_original == 'si':
        print(f"Frase original: {frase_original}")
    else:
        print("¡Hasta luego!")

if __name__ == "__main__":
    main()
