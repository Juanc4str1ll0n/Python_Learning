class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.cabeza = None

#agregar, imprimir agregar principio eliminar

    def agregar(self, dato):
        """Agrega un dato al final de la lista"""

        nuevo_dato = Nodo(dato)

        if self.cabeza == None:
            self.cabeza = nuevo_dato
        else:
            copia = self.cabeza

            while copia.siguiente:
                copia = copia.siguiente

            copia.siguiente = nuevo_dato

    def imprimir(self):
        """Imprime la lista"""

        if self.cabeza == None:
            print("La lista esta vacia")

        else:
            copia = self.cabeza
            while copia:
                print(copia.dato, "  -->  ", end=" ")
                copia = copia.siguiente
            print(" ")

    def agregar_al_principio(self, dato):
        """Agrega un dato al principio de la lista"""

        nuevo_dato = Nodo(dato)

        nuevo_dato.siguiente = self.cabeza    # Le decimos que el siguiente es la cabeza, para la referencia
        self.cabeza = nuevo_dato             #Y actualizamos la cabeza
        
        
    def eliminar(self, dato):
        """Elimina un dato especifico de la lista"""
        
        #Si la lista esta vacia
        if self.cabeza == None:
            print("No hay nada en la lista, esta vacia! ")
        
        #Si el dato esta en la cabeza
        elif self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        
        #Iterar hasta encontrar el dato
        #Creamos dos variables aux, la primera es la cabeza y la otra es el segundo dato
        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

        print("El dato no se encontro en la lista")


    def longitud(self):
        """Retorna la longitud de la lista"""
        aux = 0 

        if self.cabeza == None:
            return 0
        else:
            copia =  self.cabeza
            while copia:
                aux +=1
                copia = copia.siguiente
            return aux

    def eliminarNodo(self, num):
        """Elimina un nodo en especifico"""
        if num >= 0:
            if self.cabeza == None:
                print("La lista esta vacia")
                return
            elif num == 0:
                self.cabeza = self.cabeza.siguiente
                return
            else:
                anterior = self.cabeza
                actual = self.cabeza.siguiente
                aux = 1
                count = num

                while aux <= count:
                    if aux == num:
                        anterior.siguiente = actual.siguiente
                        return
                    else:
                        aux += 1
                        anterior = actual
                        actual = actual.siguiente 
                        print("intento")
        else:
            print("Nodo no valido, empieza desde cero en adelante")
            return
        
        print("No se encontro el nodo")
        
    def buscar(self, id):
        
        if self.cabeza == None:
            print("La lista esta vacia")
            return
        
        elif id == 0:
            return self.cabeza
        
        else:
            return



        
            
       


Estudiantes = LinkedList()

Estudiantes.agregar("Juan David")
Estudiantes.agregar("Daniel Felipe")
Estudiantes.agregar("Samuel David")
Estudiantes.agregar("Valery Juliana")
Estudiantes.agregar("Michael Jackson")
Estudiantes.agregar("Diddy")
Estudiantes.agregar_al_principio("Deivid malagan")

Estudiantes.imprimir()

Estudiantes.eliminar("Daniel Felipe")
Estudiantes.imprimir()
Estudiantes.eliminarNodo(9)
Estudiantes.imprimir()

# print(Estudiantes.longitud())

#Para entender que cada Nodo lo puedo crear y que cada nodo tiene
#Su siguiente que se debe asignar al siguiente valor

# n1 = Node(4)
# n2 = Node(5)
# n3 = Node(6)
# n4 = Node(7)

# print(id(n1))
# print(id(n2))

# n1.next = n2

# print("_______________")
# print(id(n1.next))
# print(id(n2))

