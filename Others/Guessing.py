import random
correcto = random.randint(1,50)
opcion = None
intentos = 0

while opcion != correcto:
    try:
        print("------- Bienvenido usuario ------ ")
        print("Trata de adivinar un numero del 1 al 50")
        opcion = int(input("Ingresa el numero: "))
        intentos += 1
        
        if opcion < 50 and opcion >= 0:
            if opcion == correcto:
                print(f"Felicidades! ganaste con un total de {intentos} intentos")
                break
            
            if opcion < correcto:
                print("El numero correcto es mayor")
            if opcion > correcto:
                print("El numero correcto es mennor")
        else:
            print("valor fuera del rango")
    except ValueError:
        print("Ingresa un valor valido")