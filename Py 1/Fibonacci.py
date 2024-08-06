#Fiboonacci es donde se sumen los dos numeros anteriores por ejemplo:
# 1 1 2 3 5

def fibonacci(n):
    if n < 2:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(5):
    print(fibonacci(i))


    #By Ema322 