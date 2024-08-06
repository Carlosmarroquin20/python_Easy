def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número: "))
print(f"El factorial de {numero} es {factorial(numero)}")
