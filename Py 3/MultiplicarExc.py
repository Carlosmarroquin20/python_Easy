#Multiplicar sin utilizar el *

def multipicar(a,b):
    total = 0
    for i in range(a):
        total += b
    return total

a = int(input("Ingresa el primer valor: "))

b = int(input("Ingresa el segundo valor: "))

resultado = multipicar(a,b)

print(f"El resultado de multiplicar {a} y {b} es: {resultado} ")
