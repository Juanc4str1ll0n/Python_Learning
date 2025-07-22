#La libreria collections tiene implementacion de Deque
from collections import deque

#En este caso manejo la que cree en mi paquete estructuras de datos -> Deque.py y uso mis metodos para un ejercicio
import Deque
import time

pacientes = Deque.Deque()

while True:
    print("--------------------------------")
    print("----- Gestion de pacientes -----")
    print("Que quieres hacer hoy?")
    print("1. Agregar paciente a cola")
    print("2. Agregar paciente al principio de la cola")
    print("3. Atender paciente de la cola")
    print("4. Atender el ultimo paciente")
    print("5. Voltear la fila")
    print("6. Ver fila actual")
    print("7. Comprobar nombre en fila")
    print("8. Eliminar paciente de la fila")
    print("9. Salir")
    opcion = int(input())
    
    match opcion:
        case 1:
            paciente = input("Ingresa el nombre del paciente a guardar:  ")
            pacientes.append(paciente) 
            time.sleep(1.2)
            
        case 2:
            paciente = input("Ingresa el nombre del paciente a guardar al principio de la cola:  ")
            pacientes.appendLeft(paciente)
            time.sleep(1.2)
            
        case 3:
            p = pacientes.popLeft()
            if p is None:
                print("No hay nadie en la fila")
            else:
                print("Se atendio al paciente ",p)
            time.sleep(1.2)
            
        case 4:
            p = pacientes.pop()
            if p is None:
                print("No hay pacientes en la lista")
            else:
                print("Se atendio al paciente ", p)
            
            
        case 5:
            pacientes.reverse()
            print("La lista se ha volteado")
            time.sleep(1.2)
            
        case 6:
            pacientes.print()
            time.sleep(2)
            
        case 7:
            paciente = input("Ingresa el nombre del paciente a comprobar en la cola:  ")
            
            x = pacientes.search(paciente)
            
            if x == True:
                print("Se encontro el paciente")
            else:
                print("El paciente no se encontro")
            
        case 8:
            paciente = input("Ingresa el nombre del paciente a eliminar:  ")
            pacientes.remove(paciente)
            
        case 9:
            break
        
        case _:
            print("Opcion no valida intenta de nuevo")