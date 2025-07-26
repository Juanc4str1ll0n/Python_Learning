#En un arbol binario se encuentra la raiz

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BinaryTree:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz == None:
            self.raiz = Node(valor)
        else:
            self._insertarRecursivo(Nodo_actual = self.raiz, valor =valor)   #Empezamos desde la raiz
    
    
    def _insertarRecursivo(self, Nodo_actual, valor):
        
        #Insertar a la izquierda (Es menor)
        if valor < Nodo_actual.valor:
            if Nodo_actual.izquierdo == None:
                Nodo_actual.izquierdo = Node(valor)
                return
            else:
                self._insertarRecursivo(Nodo_actual= Nodo_actual.izquierdo, valor= valor)
        
        #Insertar a la derecha (Es mayor)
        elif valor > Nodo_actual.valor:
            if Nodo_actual.derecha == None:
                Nodo_actual.derecha = Node(valor)
                return
            else:
                self._insertarRecursivo(Nodo_actual= Nodo_actual.derecho, valor= valor)
              
    #Metodo iterativo para insertar tambien es valido
    
          
    # def insertar(self, valor):
    #     nuevo = Nodo(valor)

    #     if self.raiz is None:
    #         self.raiz = nuevo
    #         return

    #     actual = self.raiz

    #     while True:
    #         if valor < actual.valor:
    #             if actual.izquierdo is None:
    #                 actual.izquierdo = nuevo
    #                 break
    #             else:
    #                 actual = actual.izquierdo
    #         elif valor > actual.valor:
    #             if actual.derecho is None:
    #                 actual.derecho = nuevo
    #                 break
    #             else:
    #                 actual = actual.derecho
    #         else:
    #             # Valor duplicado
    #             print(f"El valor {valor} ya está en el árbol.")
    #             break
    
    def esVacio(self) -> bool:
        return self.raiz == None
    
    def buscar(self, valor) -> bool:
        if self.raiz == None:
            return False
        else:
            return self._buscarRecursivo(nodo_actual= self.raiz, valor= valor)
    
    def _buscarRecursivo(self, nodo_actual, valor):
        if nodo_actual == None:
            return False
        
        if nodo_actual.valor == valor:
            return True
        
        #Buscar por la izquierda (Es menor)
        if valor < nodo_actual.valor:
            return self._buscarRecursivo(nodo_actual.izquierdo, valor)
        
        #Buscar por la derecha (Es mayor)
        if valor > nodo_actual.valor:
            return self._buscarRecursivo(nodo_actual.derecho, valor)
            
    def minimo(self):
        self._buscarMinimo(self.raiz)
                                                                
    def _buscarMinimo(self, actual):                            
        if actual == None:                                      
            return None                                         
                                                                
        if actual.izquierdo == None:                            
            return actual.valor                                
        self._buscarMinimo(actual.izquierdo)                    
    
    #--------------------------------------------
    #Buscar de forma iterativa
    # def minimo(self):
    #     actual = self.raiz
    #     while True:
    #         if actual == None:
    #             return None
    #         else:
    #             if actual.izquierdo == None:
    #                 return actual.valor
    #             else:
    #                 actual = actual.izquierdo
    #-------------------------------------------

    def size(self):
        pass
    
    def maximo(self):
        self._buscarMaximo(self.raiz)
    
    def _buscarMaximo(self, actual):
        if actual == None:
            return None
        
        if actual.derecho == None:
            return actual.valor
        self._buscarMaximo(actual.derecho)
    
    def inorden(self):
        self._inordenRecursivo(self.raiz)
    
    def _inordenRecursivo(self, nodo):
        if nodo is not None:
            self._inordenRecursivo(nodo.izquierdo)
            print(nodo.valor, end="")
            self._inordenRecursivo(nodo.derecho)
    
    def preorden(self):
        pass
    
    def _preordenRecursivo(self):
        pass
    
    def postorden(self):
        pass
    
    def postordenRecursivo(self):
        pass
    
    
    
    
    
arbolito = BinaryTree()

arbolito.insertar(9)

print(arbolito.buscar(90))
    
