class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        
class CircularDoubleLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
        
    def add(self, dato):
        """Add an element to the list"""
        nuevo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.size += 1
            #--------------------
            #Tambien serviria esto:
            #self.cabeza.siguiente = self.cola
            #self.cabeza.anterior = self.cola
            #self.cola.siguiente = self.cabeza
            #self.cola.anterior = self.cabeza
            return

        
        self.cola.siguiente = nuevo          # El nodo actual al final apunta al nuevo
        nuevo.siguiente = self.cabeza        # El nuevo apunta al principio (circularidad)
        nuevo.anterior = self.cola           # El nuevo apunta hacia atrás (doble enlace)
        self.cabeza.anterior = nuevo         # La cabeza ahora reconoce al nuevo como su anterior
        self.cola = nuevo                    # El nuevo nodo es la nueva cola
        self.size += 1
    
    def addFirst(self, dato):
        """Add an element to the beggining of the list"""
        nuevo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.size += 1
            return
        
        nuevo.siguiente = self.cabeza
        nuevo.anterior = self.cola
        self.cabeza.anterior = nuevo
        self.cola.siguiente = nuevo
        self.cabeza = nuevo
        self.size += 1
        
    def printForward(self):
        """Print the list from the Head to the Tail"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        copia = self.cabeza
        
        while True:
            print(copia.dato , " <-> ", end="")
            copia = copia.siguiente
            if copia == self.cabeza:
                break
        print()

    def printBackward(self):
        """Print the list from the Tail to the Head"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        copia = self.cola
        
        while True:
            print(copia.dato, " <-> ", end="")
            copia = copia.anterior
            if copia == self.cola:
                break
        print()
    
    def removeFirst(self):
        """Remove the first element of the list"""
        #Si la lista esta vacia 
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si solo hay un nodo
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None 
            self.size -= 1   
            return
    
        #Eliminar primero
        self.cabeza = self.cabeza.siguiente
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza
        self.size -= 1
        
    def removeLast(self):
        """Remove the last element of the list"""
        #Si la lista esta vacia 
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si solo hay un nodo
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None   
            self.size -=1 
            return
        
        #Eliminar ultimo
        self.cola = self.cola.anterior
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
        self.size -= 1
        
    def remove(self, dato):
        """Remove an specific element of the list"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si el dato esta en la cabeza
        if self.cabeza.dato == dato:
            self.removeFirst()
            return
        
        #Si el dato esta en la cola
        if self.cola.dato == dato:
            self.removeLast()
            return
        
        #Iterar en medio
        copia = self.cabeza.siguiente
        while copia!= self.cabeza:
            if copia.dato == dato:
                copia.anterior.siguiente = copia.siguiente
                copia.siguiente.anterior = copia.anterior
                return   
            copia = copia.siguiente
        
    def search(self, dato) -> bool:
        """Find an element in the list, return a Boolean"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        if self.cabeza.dato == dato:
            return True
        
        copia = self.cabeza.siguiente
        
        while copia!=self.cabeza:
            if copia.dato == dato:
                return True
            copia = copia.siguiente
            
        return False
        
    def get(self, index) :
        """Return the data of the specific index"""
        
        if self.cabeza == None:
            print("Lista vacia")
            return None
        
        if index < 0 or index > self.getSize() -1:
            print("Indice no valido")
            return None
        
        if index == 0:
            return self.cabeza.dato
        
        copia = self.cabeza.siguiente
        count = 1
        
        while count < index: 
            copia = copia.siguiente
            count += 1
             
        return copia.dato   
        
    def indexOf(self, dato) -> int:
        """Return the index of an specific data, -1 if it is not in the list"""
        if self.cabeza == None:
            return -1
        
        if self.cabeza.dato == dato:
            return 0
        
        #Iterar hasta encontrar
        index = 1
        copia = self.cabeza.siguiente
        
        while copia != self.cabeza:
            if copia.dato == dato:
                return index
            index +=1
            copia = copia.siguiente
        return -1
    
    def isEmpty(self) -> bool:
        """Boolean that describes if the list is empty"""
        return self.cabeza == None
    
    def getSize(self) -> int:
        """Return the size of the list"""
        return self.size
    
    def clear(self):
        """Remove all the elements of the Double Circular Linked list"""
        self.cabeza = None
        self.cola = None
        self.size = 0
        
    def insertAt(self, index, dato):
        """Insert an element in an specific index"""
        #Si la lista esta vacia
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Indice fuera de rango
        if index<0 or index> self.getSize():
            print("Indice no valido")
            return
        
        #Si se debe insertar al principio
        if index == 0:
            self.addFirst(dato)
            return
        
        #Si se debe insertar al final
        if index == self.getSize():
            self.add(dato)
            return
        
        #Si se debe insertar en el medio
        nuevo = Node(dato)
        count = 1
        actual = self.cabeza.siguiente
        
        while count < index:
            actual = actual.siguiente
            count +=1
        
        nuevo.anterior = actual.anterior
        actual.anterior.siguiente = nuevo
        nuevo.siguiente = actual
        actual.anterior = nuevo
        self.size += 1
        
    def toList(self) -> list:
        """Return a list of elements of the Double circular Linked List"""
        if self.cabeza == None:
            return []
        
        listica = []
        copia = self.cabeza
        for i in range(self.getSize()):
            listica.append(copia.dato)
            copia = copia.siguiente
            
        return listica


lista = CircularDoubleLinkedList()
lista.add("Avion")   
lista.add("Moto")     
lista.add("Carro")
lista.addFirst("Barco")
lista.printForward()
    
# print(lista.search("Barco"))
    
print(lista.get(1))
# print(lista.indexOf("Barco"))
# print(lista.isEmpty())

lista.insertAt(2, "Tanque")
# lista.clear()
# lista.printForward()

lista.printForward()

print(lista.toList())
# copia = lista.toList()
# print(copia)