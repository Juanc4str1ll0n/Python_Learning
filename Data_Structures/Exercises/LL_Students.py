from Data_Structures.linkedList import LinkedList

def main():
    is_Running = True
    Estudiantes = LinkedList()  # Solo se crea una vez

    while is_Running:
        print()
        print("__________________________________________")
        print("Bienvenido a la gestión de Estudiantes")
        print("__________________________________________")

        print("¿Qué quieres hacer? ")
        print("1. Agregar un estudiante")
        print("2. Agregar al principio")
        print("3. Eliminar")
        print("4. Eliminar por ID")
        print("5. Total estudiantes")
        print("6. Buscar por ID")
        print("7. Obtener ID por nombre")
        print("8. Editar estudiante")
        print("9. Imprimir estudiantes")
        print("10. SALIR")
        print("______________________________________________")

        try:
            opcion = int(input("Ingresa una opción: "))
        except ValueError:
            print("Opción inválida. Debe ser un número.")
            continue

        match opcion:
            case 1:
                dato = input("Nombre del estudiante: ")
                Estudiantes.agregar(dato)
            case 2:
                dato = input("Nombre del estudiante al principio: ")
                Estudiantes.agregar_al_principio(dato)
            case 3:
                dato = input("Nombre del estudiante a eliminar: ")
                Estudiantes.eliminar(dato)
            case 4:
                try:
                    dato = int(input("ID del estudiante a eliminar: "))
                    Estudiantes.eliminarNodo(dato)
                except ValueError:
                    print("El ID debe ser un número.")
            case 5:
                print("Total de estudiantes:", Estudiantes.longitud())
            case 6:
                dato = input("ID a buscar: ")
                Estudiantes.buscar(dato)
            case 7:
                dato = input("Nombre para obtener ID: ")
                Estudiantes.obtener_id(dato)
            case 8:
                try:
                    id = int(input("ID del estudiante a editar: "))
                    dato = input("Nuevo nombre: ")
                    Estudiantes.editarDato_id(dato, id)
                except ValueError:
                    print("El ID debe ser un número.")
            case 9:
                Estudiantes.imprimir()
            case 10:
                print("¡Hasta luego!")
                is_Running = False
            case _:
                print("Opción no válida.")

            
if __name__ == '__main__':
    main()