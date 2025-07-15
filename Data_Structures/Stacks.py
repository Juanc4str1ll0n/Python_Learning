class Node:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

class Stack:
    def __init__(self):
        self.cima = None

    def apilar(self, dato):
        """Agrega un elemento a la cima de la lista"""
        nuevo = Node(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def desapilar(self):
        """Elimina y retorna el dato de la cima"""
        if self.cima == None:
            return "Lista vacia"

        else:
            valor = self.cima.data
            self.cima = self.cima.siguiente
            return valor
        
    def verCima(self):
        "Retorna el dato de la cima sin eliminarlo"
        return self.cima.data
    
    def size(self) -> int:
        """Retorna el tamano de la lista"""
        aux = 0
        copia = self.cima

        if self.cima == None:
            return 0
        else:
            while(copia):
                aux+=1
                copia = copia.siguiente
            return aux

    def buscar(self, dato) -> bool:
        """Busca un valor y si esta devuelve true y sino devuelve false"""
        copia = self.cima

        if self.cima == None:
            return False
        
        else:
            while(copia):
                if copia.data == dato:
                    return True
                else:
                    copia = copia.siguiente
            return False

    def toList(self ) -> list:
        """Convierte el stack a una lista"""
        if self.cima ==None:
            print("Stack vacio")
        
        lista = []
        copia = self.cima

        while(copia):
            lista.append(copia.data)
            copia = copia.siguiente

        return lista

    def isEmpty(self) -> bool:
        """Retorna true si la lista esta vacia y False si la lista tiene datos"""
        return self.cima == None

    def imprimir(self):
        """Imprime la lista"""
        copia = self.cima

        while(copia):
            print(copia.data)
            copia = copia.siguiente

    def vaciar(self):
        """Vacía por completo la pila"""
        if self.cima is None:
            print("La pila ya está vacía.")
        else:
            self.cima = None
            print("Pila vaciada correctamente.")

s = Stack()

s.apilar(1)
s.apilar(2)
s.apilar(3)
s.imprimir()

print(s.size())
print(s.buscar(99))

myList = s.toList()

print(myList)