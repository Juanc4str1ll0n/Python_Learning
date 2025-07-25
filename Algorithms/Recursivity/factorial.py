#Factorial de un numero

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)  #La funcion retorna un valor y ese valor lo multiplica por el num


print(factorial(2))


