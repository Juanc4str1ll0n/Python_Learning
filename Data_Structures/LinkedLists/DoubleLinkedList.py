# Cada vez que se agrega un nuevo nodo, se deben actualizar dos referencias:
#  una hacia adelante (siguiente)
#  y una hacia atrás (anterior)
class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.anterior = None

class DoublyLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.count = 0

    def Add(self, dato):
        """Agregar un dato al final de la lista enlazada doble"""
        nuevo = Node(dato)
        #Si la lista esta vacia 
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            self.count += 1
            return
        #Implementacion al final
        self.cola.siguiente = nuevo   #Referencia hacia adelante
        nuevo.anterior = self.cola    #Referencia hacia atras
        self.cola = nuevo    #DE ULTIMAS se actualiza la cola 
        self.count += 1
        


    def AddFirst(self, dato):
        """Agregar dato al principio"""
        nuevo = Node(dato)

        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            self.count += 1
            return

        self.cabeza.anterior = nuevo
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.count += 1

    def print(self):
        """Imprimir lista"""

        if self.cabeza == None:
            print("Lista vacia, error")
            return
        copia = self.cabeza
        while(copia != None):
            print(copia.data, " <-> ", end="")
            copia = copia.siguiente
        print()

    def getSize(self) -> int:
        """Retorna el tamano de la lista"""
        return self.count
    
    def removeFirst(self):
        """Elimina el primer dato"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            return
        
        self.cabeza = self.cabeza.siguiente
        self.cabeza.anterior = None         #Eliminamos la referencia al dato de la cabeza, si no sigue quedando
        

    def removeLast(self):
        """Elimina el ultimo dato"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            return
        
        self.cola = self.cola.anterior
        self.cola.siguiente = None

    def search(self, dato) -> bool:
        """Busca un valor en la lista"""
        copia = self.cabeza

        if self.cabeza == None:
            return False
        
        while copia:
            if copia.data == dato:
                return True
            copia = copia.siguiente
        return False

    def remove(self, dato):
        """Elimina el primer dato que coincida"""

        #Si la lista esta vacia
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si el dato esta en la cabeza
        if self.cabeza.data == dato:
            self.removeFirst()
            return
        
        #Si el dato esta en la cola
        if self.cola and self.cola.data == dato:
            self.removeLast()
            return
        
        #Buscar en la lista
        actual = self.cabeza.siguiente
        while actual:
            if actual.data == dato:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente
        print("No se encontro a ", dato)

    def insertAt(self, dato, posicion):
        size = self.getSize()

        if posicion < 0 or posicion > size():
            print("Posición inválida")
            return

        nuevo = Node(dato)

        # Insertar al inicio
        if posicion == 0:
            self.AddFirst(dato)
            return

        # Insertar al final
        if posicion == size:
            self.Add(dato)
            return

        # Insertar en el medio
        actual = self.cabeza
        index = 0
        while index < posicion:
            actual = actual.siguiente
            index += 1

        nuevo.anterior = actual.anterior
        nuevo.siguiente = actual
        actual.anterior.siguiente = nuevo
        actual.anterior = nuevo

    def clear(self):
        if self.cabeza == None:
            return
        self.cabeza = None
        self.cola = None

    def getId(self, dato) -> int:
        
        if self.cabeza == None:
            print("Lista vacia error")
            return
        
        if self.cabeza.data == dato:
            return 0
        
        copia = self.cabeza.siguiente
        count = 1

        while copia:
            if copia.data == dato:
                return count
            count += 1
            copia = copia.siguiente

        print("Dato no encontrado")

Estudiantes = DoublyLinkedList()

Estudiantes.Add("Juan")
Estudiantes.Add("Valery")
Estudiantes.AddFirst("Mia")
Estudiantes.Add("Santiago")
Estudiantes.Add("Samuelito")

Estudiantes.print()

tamano = Estudiantes.getSize()
print("el tamano es",tamano)

Estudiantes.remove("Samuelito")
Estudiantes.print()
print(Estudiantes.getId("Santiago"))


