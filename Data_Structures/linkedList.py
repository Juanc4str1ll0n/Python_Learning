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



# Estudiantes = LinkedList()

# Estudiantes.agregar("Juan David")
# Estudiantes.agregar("Daniel Felipe")
# Estudiantes.agregar("Samuel David")
# Estudiantes.agregar("Valery Juliana")
# Estudiantes.agregar_al_principio("Deivid malagan")

# Estudiantes.imprimir()

# Estudiantes.eliminar("Daniel Felipe")
# Estudiantes.imprimir()

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

