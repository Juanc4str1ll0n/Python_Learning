class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class CircularLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def add(self, dato):
        """Add an element at the end of the list"""
        nuevo = Node(dato)

        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo   #Importante si esta vacia que apunte a si misma para cerrar el circulo
            self.size += 1
            return
        
        nuevo.siguiente = self.cola.siguiente
        self.cola.siguiente = nuevo
        self.cola = nuevo
        self.size += 1
        
    
    def addFirst(self, dato):
        """Add an element at the beggining of the list"""
        nuevo = Node(dato)

        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = nuevo
            nuevo.siguiente = nuevo 
            self.size += 1  
            return
        
        nuevo.siguiente = self.cabeza
        self.cola.siguiente = nuevo
        self.cabeza = nuevo
        self.size += 1

    def print(self):
        """Print the list"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        actual = self.cabeza
        while True:                                 #La forma de imprimir una lista circular es diferente a las anteriores
            print(actual.data , " -> ", end="")     #Esto debido a que la lista siempre se encuentra conectada mediante nodos
            actual = actual.siguiente               #Se crea un ciclo que cierra cuando el dato sea igual a la cabeza
            if actual == self.cabeza:
                break
        print()
     
    def remove(self, dato):
        """Delete an specific element of the list"""        
        #Si la lista esta vacia
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si el dato esta en la cabeza
        if self.cabeza.data == dato:
            self.removeFirst()
            return
        
        #Si el dato esta de ultimas 
        if self.cola.data == dato:
            self.removeLast()
            return
        
        #recorrer
        anterior = self.cabeza
        actual = self.cabeza.siguiente
        
        while actual != self.cabeza:
            if actual.data == dato:
                anterior.siguiente = actual.siguiente
                return
            
            anterior = actual
            actual = actual.siguiente
            
        print("No se encontro el dato")
        
           
    def removeFirst(self):
        """Remove the first element of the list"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        
        #Si solo hay un nodo:
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            self.size -= 1
            return
        
        self.cola.siguiente = self.cabeza.siguiente
        self.cabeza = self.cabeza.siguiente
        self.size -= 1
    
    def removeLast(self):
        """Remove the last element of the list""" 
        if self.cabeza == None:
           print("Lista vacia")
           return
        
        #Si hay un solo nodo
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            self.size -= 1
            return
        
        #Iterar hasta encontrar el anterior de la cola
        actual = self.cabeza
        
        while actual.siguiente != self.cola:
            actual = actual.siguiente
            
        actual.siguiente = self.cola.siguiente
        self.cola = actual
        self.size -= 1
         
    def toList(self) -> list:
        """Converts the circular list to a normal List"""
        myList = []

        if self.cabeza == None:
            return []
        
        actual = self.cabeza
        while True:
            myList.append(actual.data)
            actual = actual.siguiente
            if actual == self.cabeza:
                break
            
        return myList 
    
    def search(self, data) -> bool:
        """Find out if an element exists in the list"""
        if self.cabeza == None:
            return False
        
        actual = self.cabeza 
        while True:
            if actual.data == data:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        
        return False         
    
    def clear(self):
        """Remove all the elements of the list"""
        if self.cabeza == None:
            print("Lista ya se encuentra vacia")
            return
        
        self.cabeza = None
        self.cola = None
    
    def isEmpty(self) -> bool:
        """Return True if the list is Empty, False if it isn't"""
        return self.cabeza == None
    
    def getSize(self) -> int:
        """Return the size of the list"""
        return self.size
    
    def getFirst(self):
        """Return the first element of the list"""
        return self.cabeza.data
    
    def getLast(self):
        """Return the last element of the list"""
        return self.cola.data
    
lista = CircularLinkedList()
lista.add("Valery")
lista.add("Juan")
lista.add("Samuelito")
lista.add("Hola")
lista.addFirst("Danielito")

lista.print()

listica = lista.toList()
print(listica)

size = lista.getSize()
print(size)

print(lista.isEmpty())

# lista.clear()
lista.print()
print(lista.search("Valery"))
lista.remove("Holakjhdsa")
lista.print()