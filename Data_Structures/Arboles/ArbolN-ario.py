# Un árbol N-ario es una estructura jerárquica donde cada nodo tiene hasta N hijos. 
# Se representa con una lista de hijos y se usa en estructuras como Tries, árboles de archivos, 
# árboles de juegos y más. Son útiles para representar jerarquías generales sin el límite de dos hijos
# como en los árboles binarios.
import json
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
        self.size = 1
    
    #Esta es la forma base de insertar un nodo en su padre,
    #La unica cosa es que se insertar desordenadamente, esto depende de la funcion del programa
    #----------------------------------------------------------------
    def insertarRecursivo2(self, nodo_actual, padre, valor):
        if nodo_actual == None:
            return
        
        if nodo_actual.valor == padre:
            nodo_actual.hijos.append(Node(valor))
            self.size +=1
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
            self.size += 1
            return
        
        insertado = False
        
        for i in range(len(nodo.hijos)):
            if valor < nodo.hijos[i].valor:
                nodo.hijos.insert(i, nuevo)
                insertado = True
                self.size += 1 
                break
            
        if insertado == False:
            nodo.hijos.append(nuevo)
            self.size += 1
            
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
    
    def isEmpty(self)-> bool:
        return self.raiz == None
    
    def aListaPreorden(self) -> list:
        resultado = []
        self.__aListaPreorden(self.raiz, resultado)
        return resultado
    
    def __aListaPreorden(self, actual, lista):
        #Raiz izquierdo derecho 

        if actual == None:
            return
        
        lista.append(actual)
        
        for hijo in actual.hijos:
            self.__aListaPreorden(hijo, lista)
        return
    
    def altura(self):
        return self.__alturaRecursiva(self.raiz)
    
    def __alturaRecursiva(self, actual):
        if actual is None:
            return 0
        
        if not actual.hijos:
            return 1
        return 1 + max(self.__alturaRecursiva(hijo) for hijo in actual.hijos)

    def contarNodos(self) -> int:
        return self.size
    
    def aDiccionario(self):
        return self.__aDiccionarioRecursivo(self.raiz)
    
    def __aDiccionarioRecursivo(self, actual) -> dict:
        if actual == None:
            return 
        
        return{
            "Valor" : actual.valor,
            "Hijos" : [self.__aDiccionarioRecursivo(hijo) for hijo in actual.hijos]
        }

 
    #En este modo voy a hacer que solo se elimine el nodo y los hijos de el pasen a ser hijos del padre del nodo eliminado
    def eliminarNodo(self, dato):
        if self.raiz == None:
            print("No se puede eliminar nada el arbol esta vacio")
            return
        
        if self.raiz == dato:
            print("No se puede eliminar la raiz, llama al otro metodo")
            return 
        
        eliminado = self.__eliminarNodoRecursivo(dato, self.raiz)
        if eliminado == False:
            print("No se encontro el nodo a eliminar")
    
    def __eliminarNodoRecursivo(self, dato, actual):
        for i, hijo in enumerate(actual.hijos):
            if hijo.valor == dato:
                
                #Reasignar los hijos del dato que se elimina poniendolos en la lista del abuelo
                #Del padre del nodo que se elimino
                for nieto in hijo.hijos:
                    self.__insertarOrdenados(actual, nieto)
                
                #Eliminamos el nodo
                del actual.hijos[i]
                self.size -= 1
                return True
                
            else:
                eliminado = self.__eliminarNodoRecursivo(dato, hijo)
                if eliminado == True:
                    return True
        
        return False
    
    #En esta funcion si el nodo a eliminar tiene hijos estos tambien seran eliminados
    #Es decir se elimina toda la rama o subarbol
    
    def eliminarCompleto(self, dato):
        if self.raiz == None:
            print("Arbol vacio")
            return
        
        if self.raiz == dato:
            print("No se puede eliminar la raiz directamente")
            return
        
        self.__eliminarrecursivo(self.raiz, dato)
    
    def __eliminarrecursivo(self, actual, dato):
        for i, hijo in enumerate(actual.hijos):
            if hijo.valor == dato:
                del actual.hijos[i]
                print("Eliminado arbol") 
                return True
            else:
                eliminado = self.__eliminarrecursivo(hijo, dato)    
                if eliminado:
                    return True
            
#En este caso la raiz tomara su primer hijo y lo promovera a raiz (Esto no sigue una regla, depende de la implementacion del programa)
    def eliminarRaiz(self): 
        if self.raiz == None:
            return
        
        #Si la raiz no tiene hijos, el arbol queda vacia
        if len(self.raiz.hijos) == 0:
            self.raiz = None
            self.size -= 1
            print("Se elimino la raiz")
            return

        #Escoger el primer hijo de la raiz
        nueva = self.raiz.hijos[0]
        
        #Asignar la nueva raiz
        self.raiz.valor = nueva.valor
        
        #Eliminamos el hijo 0 que promovimos a raiz
        del self.raiz.hijos[0]
        self.size -= 1
        
        #Agregar los hijos del que eliminamos en los hijos de la nueva raiz
        for hijos in nueva.hijos:
            self.__insertarOrdenados(self.raiz, hijos.valor)
        
        print(f"La raiz fue eliminada, la nueva raiz es {self.raiz.valor}")
        
        
    
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

print("SIZE")
print(arbolito.contarNodos())

print("ALTURA")
print(arbolito.altura())
diccionario = arbolito.aDiccionario()


#-----------------------------------------------------
#           CONVIRTIENDOLOS A JSON
# jsonStr = json.dumps(diccionario, indent=2)
# print(jsonStr)

# url = "Data_Structures/Arboles/prueba.json"
# with open(url, "w") as jsiton:
#     jsiton.write(jsonStr)
    
#-----------------------------------------------------

arbolito.eliminarRaiz()
arbolito.recorridoPorNiveles()