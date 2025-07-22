# Diferencia entre Queue y Deque:
# - Queue (Cola): estructura de datos FIFO (First-In, First-Out).
#   Solo permite insertar elementos por el final (enqueue) y eliminarlos por el frente (dequeue).
#   Ejemplo típico: fila del supermercado.

# - Deque (Double Ended Queue o Cola Doble): estructura más flexible que permite inserciones
#   y eliminaciones tanto por el frente como por el final.
#   Soporta operaciones como: insertar al inicio (offerFirst), insertar al final (offerLast),
#   eliminar del inicio (pollFirst) y eliminar del final (pollLast).
#   Es útil para casos donde se necesita tanto comportamiento FIFO como LIFO.
#   Tiene la esrtructura de una lista enlazada doble
#   Esta pensada para hacer operaciones por derecha e izquierda

class Node:
    def __init__(self, dato):
        self.data = dato
        self.siguiente = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
        
    def append(self, dato):
        """Append an element to the end of the Queue"""
        nuevo = Node(dato)
        
        if self.inicio == None:
            self.inicio = nuevo
            self.final = nuevo
            nuevo.anterior = None
            nuevo.siguiente = None
            self.size += 1
            return
        
        nuevo.anterior = self.final      # Enlace poniendo el nuevo de ultimas, despues del final de la cola
        self.final.siguiente = nuevo     #Enlace del final de la cola al siguiente, recordando que estamos manejando doble enlace
        self.final = nuevo               #Actualizamos la cola
        self.size +=1    
    
    def appendLeft(self, dato):
        """Append an element at the Beggining of the list"""
        nuevo = Node(dato)
        
        if self.inicio == None:
            self.inicio = nuevo
            self.final = nuevo
            nuevo.anterior = None
            nuevo.siguiente = None
            self.size +=1
            return
        
        nuevo.siguiente = self.inicio
        self.inicio.anterior = nuevo
        self.inicio = nuevo
        self.size+=1
    
    def pop(self):
        """Remove the last element and returns it"""
        
        if self.inicio == None:
            return None
        
        #Si solo hay un nodo en la cola
        if self.inicio == self.final:
            copia = self.inicio.data
            self.inicio = None
            self.final = None
            self.size -= 1
            return copia
        
        copia = self.final.data
        self.final = self.final.anterior
        self.final.siguiente = None
        self.size -=1
        
        return copia
    
    def popLeft(self):
        """Remove an element at the beggining of the list and returns it"""
        if self.inicio == None:
            return None
        
        if self.inicio == self.final:
            copia = self.inicio
            self.inicio = None
            self.final = None
            self.size -=1
            return copia.data
        
        copia = self.inicio
        self.inicio = self.inicio.siguiente
        self.inicio.anterior = None
        self.size -=1
        
        return copia.data
    
    def isEmpty(self) -> bool:
        """Returns a boolean that determines if the list is empty"""
        return self.inicio == None
    
    def getSize(self) -> int:
        """Return the size of the queue"""
        return self.size
    
    def reverse(self):
        """Reverse the queue"""
        actual = self.inicio
        
        while actual != None:
            siguiente = actual.siguiente
            
            #Intercambiar los punteros de cada nodo: anterior y siguiente
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior            
            #Avanzar
            actual = siguiente
        #Cambiar la cabeza y el final
        self.inicio, self.final = self.final, self.inicio
        
    def print(self):
        if self.inicio == None:
            print("Lista vacia")
            
        else:
            copia = self.inicio
            while copia:
                print(copia.data ," <-> ", end="")
                copia = copia.siguiente
            print()
    
    def remove(self, dato):
        """Remove an specific element of the list"""
        
        if self.inicio == None:
            print("Lista vacia")
            return
        
        if self.inicio == self.final and self.inicio.data == dato:
            self.inicio = None
            self.final = None
            self.size -=1
            return
        
        if self.inicio.data == dato:
            self.popLeft()
            return
        
        if self.final.data == dato:
            self.pop()
            return
        
        copia = self.inicio
        
        while copia:
            if copia.data == dato:
                copia.anterior.siguiente = copia.siguiente
                copia.siguiente.anterior = copia.anterior
                self.size -=1
                return
            copia = copia.siguiente      
        
    def search(self, dato) -> bool:
        """Search an element on the Deque"""
        nodo = Node(dato)
        
        if self.inicio == None:
            print("Lista vacia")
            return
        
        if self.inicio.data == dato:
            return True
        
        if self.final.data == dato:
            return True
        
        #Iterar
        copia = self.inicio.siguiente
        
        while copia:
            if copia.data == dato:
                return True
            copia = copia.siguiente
        return False
                
        
                    
estudiantes = Deque()

estudiantes.append("Juan")
estudiantes.append("David")
estudiantes.appendLeft("Maria")
estudiantes.appendLeft("Mario")

estudiantes.print()

# estudiantes.pop()
# estudiantes.popLeft()
estudiantes.print()

estudiantes.reverse()
estudiantes.print()

print(estudiantes.search("juanito el golondrina"))