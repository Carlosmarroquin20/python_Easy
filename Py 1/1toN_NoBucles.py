#Numero del 1 a N sin usar bucles

def pec(i,n):
    if i <= n:
        print(i)
        i+=1
        pec(i,n)

pec(1,3)


#By Ema322 