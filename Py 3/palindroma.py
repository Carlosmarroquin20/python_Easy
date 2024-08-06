def es_capicua(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para una comparación insensible a mayúsculas
    return palabra == palabra[::-1]  # Comparar la palabra con su reverso

# Solicitar una palabra al usuario
palabra = input("Introduce una palabra: ")

# Verificar si la palabra es capicúa y mostrar el resultado
if es_capicua(palabra):
    print(f"{palabra} es capicúa.")
else:

    print(f"{palabra} no es capicúa.")







