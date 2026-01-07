#Exception = An event that interrupts the flow of a program
            # ZeroDivisionError, TypeError, ValueError
            #1. Try  2. Except 3. Finally 

#Base


#Ejemplo 1

try:
    x=10/0
except Exception as e:
    print("Ocurrio un error: ", e)

finally:
    print("Esto siempre se ejecuta (finalizacion)")

print("---------------------------------------------")

#Ejemplo2