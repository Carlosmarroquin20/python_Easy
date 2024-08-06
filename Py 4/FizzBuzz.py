"""
Para los números divisibles por 3, imprimirá "Fizz".
Para los números divisibles por 5, imprimirá "Buzz".
Para los números divisibles por ambos 3 y 5, imprimirá "FizzBuzz".
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
