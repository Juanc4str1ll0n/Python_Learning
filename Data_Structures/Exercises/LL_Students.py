from ...Data_Structures.linkedList import LinkedList

def main():

    Estudiantes = LinkedList()

    print("__________________________________________")
    print("Bienvenido a la gestion de Estudiantes")
    print("__________________________________________")

    print("Que quieres hacer? ")
    print("1. Agregar un estudiante")
    print("2. Agregar a un estudiante al principio")
    print("3. Eliminar un estudiante")
    print("4. Eliminar estudiante por id")
    print("5. Obtener total de estudiantes")
    print("6. Buscar estudiante por id")
    print("7. Obtener id de estudiante")
    print("8. Editar estudiante")
    print("9. Imprimir estudiantes")
    print("10. SALIR ")
    print("______________________________________________")
    opcion = int(input())

    match opcion:
        case 1:
            dato = input("Ingresa el nombre del estudiante a guardar")
            Estudiantes.agregar(dato)
            
        case 2:
            dato = input("Ingresa el nombre del estudiante a guardar de primero")
            Estudiantes.agregar_al_principio(dato)

        case 3:
            dato = input("Ingresa el nombre del estudiante a ELIMINAR")
            Estudiantes.eliminar(dato)

        case 4:
            try: 
                dato = int(input("Ingresa el id del estudiante a ELIMINAR"))
                Estudiantes.eliminarNodo(dato)
            except ValueError:
                print("Error, el id deberia ser un numero")

        case 5:
            print("El total de estudiantes es de: ", Estudiantes.longitud())

        case 6:
            dato = input("Ingresa el id del estudiante a buscar")
            Estudiantes.buscar(dato)

        case 7:
            pass
        case 8:
            pass
        case 9:
            Estudiantes.imprimir()
        case 10:
            return

if __name__ == '__main__':
    main()