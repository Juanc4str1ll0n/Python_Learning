# Un árbol N-ario es una estructura jerárquica donde cada nodo tiene hasta N hijos. 
# Se representa con una lista de hijos y se usa en estructuras como Tries, árboles de archivos, 
# árboles de juegos y más. Son útiles para representar jerarquías generales sin el límite de dos hijos
# como en los árboles binarios.
from collections import deque

class Node:
    def __init__(self, data):
        self.valor = data
        self.hijos = []
        
    def __str__(self):
        return str(self.valor)
        
class NTree:
    def __init__(self, valor_raiz):
        self.raiz = Node(valor_raiz)
    
    #Esta es la forma base de insertar un nodo en su padre,
    #La unica cosa es que se insertar desordenadamente, esto depende de la funcion del programa
    #----------------------------------------------------------------
    def insertarRecursivo2(self, nodo_actual, padre, valor):
        if nodo_actual == None:
            return
        
        if nodo_actual.valor == padre:
            nodo_actual.hijos.append(Node(valor))
            return
        
        for hijo in nodo_actual.hijos:
            self.insertarRecursivo(hijo, padre, valor)
    #------------------------------------------------------------  
    
    
    #En este caso vamos a implementar que los hijos dentro de la lista de hijos se agreguen ordenadamente
      
    def insertar(self, padre,  valor):
        if self.buscar(valor) is not None:
            print("No se permiten valores duplicados")
        
        if self.raiz == None:
            return 
        elif self.raiz == padre:
            self.__insertarOrdenados(self.raiz, valor)
            return
        else:
            self.__insertarRecursivo(self.raiz, padre, valor)
            return
            
    def __insertarRecursivo(self, nodo_actual, padre, valor):
        if nodo_actual == None:
            return
        if nodo_actual.valor == padre:
            self.__insertarOrdenados(nodo_actual, valor)
            return
        
        for hijo in nodo_actual.hijos:
            self.__insertarRecursivo(hijo, padre, valor)
    
    def __insertarOrdenados(self, nodo, valor):
        nuevo = Node(valor)
        
        if len(nodo.hijos) == 0:
            nodo.hijos.append(nuevo)
            return
        
        insertado = False
        
        for i in range(len(nodo.hijos)):
            if valor < nodo.hijos[i].valor:
                nodo.hijos.insert(i, nuevo)
                insertado = True
                break
            
        if insertado == False:
            nodo.hijos.append(nuevo)
            
    #Buscar busca un nodo y lo retorna, con este nodo retornado podremos acceder
    #  a sus hijos a su valor y hacerle lo que se necesite NO retorna TRue o false Si no lo encuentra retorna None
    
    def buscar(self, valor):
        return self.__buscarRecursivo(self.raiz, valor)
    
    def __buscarRecursivo(self, nodo_actual , valor ):
        if nodo_actual == None:
            return None
        
        if nodo_actual.valor == valor:
            return nodo_actual
        
        for hijo in nodo_actual.hijos:
            resultado = self.__buscarRecursivo(hijo, valor)
            if resultado is not None:
                return resultado
        
        return None
    
    def preorden(self):
        if self.raiz == None:
            return
        self.__preordenRecursivo(self.raiz)
        
    def __preordenRecursivo(self, actual):
        # raiz iz derecho
        if actual == None:
            return
        
        print(actual.valor, end=" - ")
        
        for hijo in actual.hijos:
            self.__preordenRecursivo(hijo)
        
    def postorden(self):
        #izquierda derecha raiz 
        if self.raiz == None:
            return 
        self.__postordenRecursivo( self.raiz)
    
    def __postordenRecursivo(self, actual):
        if actual == None:
            return
        
        for hijo in actual.hijos:
            self.__postordenRecursivo(hijo)
        
        print(actual.valor, end=" - ")
    
    
    def recorridoPorNiveles(self):
        if self.raiz == None:
            return
        
        cola = deque()
        cola.append(self.raiz)
        
        while cola:
            nodo_actual = cola.popleft()
            
            print(nodo_actual.valor, end=" - ")
            
            for hijo in nodo_actual.hijos:
                cola.append(hijo)
                
arbolito = NTree(38)

arbolito.insertar(38, 15)
arbolito.insertar(38, 20)
arbolito.insertar(38, 30)
arbolito.insertar(38, 40)

arbolito.insertar(15, 9)
arbolito.insertar(15, 23)
arbolito.insertar(15, 22)
arbolito.insertar(15, 8)
arbolito.insertar(15, 31)

arbolito.insertar(9, 10)
arbolito.insertar(9, 11)
arbolito.insertar(9, 12)

arbolito.insertar(20, 25)
arbolito.insertar(20, 26)

arbolito.insertar(30, 32)
arbolito.insertar(30, 34)
arbolito.insertar(30, 36)

arbolito.insertar(40, 41)
arbolito.insertar(40, 42)
arbolito.insertar(40, 43)
arbolito.insertar(40, 44)


arbolito.insertar(43, 50)
arbolito.insertar(43, 51)

arbolito.insertar(51, 52)


arbolito.preorden()
arbolito.postorden()


print("RECORRIDO POR NIVELES")
arbolito.recorridoPorNiveles()