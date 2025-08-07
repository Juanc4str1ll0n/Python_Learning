# Un Trie, también conocido como árbol de prefijos, es una estructura de datos que se utiliza principalmente 
# para almacenar cadenas de texto de manera eficiente, especialmente cuando se trabaja con grandes conjuntos 
# de palabras, como diccionarios o autocompletado.
# 🌳 Características principales de un Trie
# - Cada nodo representa un carácter de una cadena.
# - Las rutas desde la raíz hasta los nodos finales representan palabras completas.
# - No almacena directamente las cadenas, sino los prefijos compartidos entre ellas.
# - Es ideal para realizar búsquedas rápidas de palabras, prefijos o sugerencias.
# 🔍 ¿Para qué se usa un Trie?
# - Autocompletar (como en motores de búsqueda o apps de mensajería)
# - Corrección ortográfica
# - Búsqueda por prefijos
# - Compresión de datos en algunas variantes

class Node:
    def __init__(self):
        self.hijos = {}  #Cada nodo tiene indefinidos hijos
        self.esFinal = False   #True si es el final de una palabra
        
class Trie:
    def __init__(self):
        self.raiz = Node()
        self.size = 0
    
    def insertar(self, palabra:str):
        if not palabra:
            return
        
        #Iterar sobre la palabra agregando el nodo y pasando de nodo en nodo
        actual = self.raiz
        for letra in palabra:
            if letra not in actual.hijos:
                actual.hijos[letra] = Node()
            actual = actual.hijos[letra]
        actual.esFinal = True
        self.size +=1          
    
    def buscar(self, palabra:str) -> bool:
        if not palabra:
            return False
        
        actual = self.raiz
        for letra in palabra:
            if letra not in actual.hijos:
                return False
            actual = actual.hijos[letra]
        return actual.esFinal     

    #-----------------------------------------------
    #Metodo base para comprobar si una palabra empieza por una letra especifica
    def __iniciaCon(self, letra:str)-> bool:
        if not self.raiz.hijos:
            return False
        elif letra in self.raiz.hijos:
            return True
        else:
            return False
    #------------------------------------------------  
    def iniciaCon(self, prefijo:str) -> bool:
        actual = self.raiz
        
        for letra in prefijo: 
            if letra not in actual.hijos:
                return False
            actual = actual.hijos[letra]
        return True
        
    #Con recursividad para recorrer todo
    def listarPalabras(self) -> list:
        resultado = []
        self.__DFS(self.raiz, "", resultado) 
        return resultado
    
    def __DFS(self, actual, recorrido, resultado):   #Depth first search
        #Si terminamos de recorrer la palabra 
        if actual.esFinal:
            resultado.append(recorrido)
        
        #Recorremos todos los hijos del nodo actual
        for letra, nodo in actual.hijos.items():
            # Llamamos recursivamente, agregando la letra actual al camino
            self.__DFS(nodo, recorrido + letra, resultado )
    
    def listarConPrefijo(self, prefijo:str) -> list:
        actual = self.raiz
        
        #1. Navegar hasta el nodo final del prefijo
        for letra in prefijo:
            if letra not in actual.hijos:
                return []
            actual = actual.hijos[letra]
        
        #Ahora buscamos recursivamente desde ese punto
        resultado = []
        self.__DFS2(actual, prefijo, resultado)
        return resultado
        
    
    def __DFS2(self, nodo, camino, resultado):
        if nodo.esFinal:
            resultado.append(camino)
        
        for letra, node in nodo.hijos.items():
            self.__DFS2(node, camino + letra, resultado)
        
    def eliminar(self, palabra):
        if not self.buscar(palabra):
            return
        self.__eliminar(self.raiz, palabra, 0)

    def __eliminar(self, nodo, palabra, index):
            
            if len(palabra == index):
                nodo.esFinal = False
                return len(nodo.hijos) == 0

            letra = palabra[index]
            if letra not in nodo.hijos:
                return False
            
            nodo_hijo = nodo.hijos[letra]
            puedeEliminarHijo = self.__eliminar(nodo_hijo, palabra, index + 1)
            
            if puedeEliminarHijo:
                del nodo.hijos[letra]
                return len(nodo.hijos) == 0 and not nodo.esFinal
            return False
            
    def esVacio(self) -> bool:
        return not self.raiz.hijos
    
    def getSize(self) -> int:
        return self.size

    
mini = Trie()
mini.insertar("Gato")
mini.insertar("Gaturro")
mini.insertar("Carro")
mini.insertar("Gatuno")
mini.insertar("Gatito")
mini.insertar("Casa")
mini.insertar("Casino")

print(mini.buscar("Gaturro"))
print(mini.buscar("Gat"))
print(mini.buscar("hola"))
print(mini.buscar("Carro"))
print(mini.getSize())

print(mini.listarPalabras())
print(mini.listarConPrefijo("Ca"))