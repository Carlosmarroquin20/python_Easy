#Easy Calculator en py

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
operacion = input("Introduce una operación (+ - * /): ")

match operacion:
    case "+":
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
    case _:
        res = None
        print("Operación no válida. Por favor, introduce una operación válida (+ - * /).")

if res is not None:
    print(f"El resultado de {num1} {operacion} {num2} es {res}")
