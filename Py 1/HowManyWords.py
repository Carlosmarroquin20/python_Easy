#Se pide una frase y se devuelve cuantas palabras tiene

def contar():
    frase = input("Escribe la frase: ")
    palabras = frase.split(" ")
    return len(palabras)

print(contar())


#By Ema322 