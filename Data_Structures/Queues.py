#QUEUE -> COLAS
#ESTRUCTURA DE DATOS QUE SIGUE EL PRNCIPIO FIFO
#FIRST IN FIRST OUT
#Es como una fila de banco el primero que llega sale primero el que va llegando se pone al final de la cola

class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Queue:
    def __init__(self):
        self.cabeza = None
        self.size = 0

    def encolar(self, data):
        """Agrega a la cola"""
        nuevo = Node(data)

        if self.cabeza == None:
            self.cabeza = nuevo
            self.size +=1
            return
        else:
            copia = self.cabeza
            
            while copia.siguiente:
                copia = copia.siguiente
            self.size += 1 
            copia.siguiente = nuevo
            
    def contains(self, data) -> bool:
        """Comprueba si un valor esta en la cola"""
        if self.cabeza == None:
            return False
        copia = self.cabeza
        while copia:
            if copia.data == data:
                return True
            else:
                copia = copia.siguiente
        return False

    def clone() :
        pass

    def eliminarEspecifico(self, dato):
        """Elimina und ato especifico de la cola"""
        if self.cabeza == None:
            print("Cola vacia")
            return
        
        #Si el nodo esta en la cabeza
        if self.cabeza.data == dato:
            self.cabeza = self.cabeza.siguiente
            self.size -= 1
            return
        else:
            anterior = self.cabeza
            actual = self.cabeza.siguiente

            while actual:
                if actual.data == dato:
                    anterior.siguiente = actual.siguiente
                    self.size -=1
                    return
                anterior = actual
                actual = actual.siguiente
            print("Dato no encontrado")



    def desencolar(self):
        """Elimina el primer valor y lo retorna"""
        if self.cabeza == None:
            print("Lista vacia")
            return
        else:
            valor = self.cabeza.data
            self.cabeza = self.cabeza.siguiente
            self.size -= 1
        return valor

    def peek(self):
        """Retorna el valor del principio de la cola"""
        if self.cabeza == None:
            return None
        
        return self.cabeza.data

    def imprimir(self):
        """Imprime la cola, el primer valor es la cima"""
        if self.cabeza == None:
            print("La cola esta vacia ")
            return
        
        copia = self.cabeza

        while copia:
            print(copia.data ," -> ", end=" ")
            copia = copia.siguiente
        print()
        
    def getSize(self) -> int:
        """Retorna el size de la cola"""
        return self.size
    
    def isEmpty(self) -> bool:
        """Retorna true si esta vacia la cola, de lo contrario False"""
        return self.cabeza == None
    
    def toList(self) -> list:
        """Convierte la cola en una lista"""
        if self.cabeza == None:
            return []
        
        myList = []
        copia = self.cabeza

        while copia:
            myList.append(copia.data)
            copia = copia.siguiente
        return myList
    
    def fromList(self, list: list):
        """Recibe una lista y la encola con los datos de la cola"""
        for item in list:
            self.encolar(item)
        
    
cola = Queue()

cola.encolar("Juan")
cola.encolar("Valery")
cola.encolar("Mia")
cola.encolar("Juan2")
cola.imprimir()
print(cola.getSize())

cola.eliminarEspecifico("Mia")
cola.eliminarEspecifico("Valery")

cola.imprimir()
print(cola.getSize())