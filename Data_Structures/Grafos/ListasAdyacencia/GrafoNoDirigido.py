"""
Un grafo no dirigido es una estructura compuesta por un conjunto de vértices (nodos) y un conjunto de aristas (conexiones) 
que enlazan pares de vértices. A diferencia de los grafos dirigidos, las aristas no tienen dirección: si existe una conexión 
entre A y B, entonces se puede ir de A a B y también de B a A.

Características principales de un grafo no dirigido:
- Las aristas representan relaciones bidireccionales.
- La estructura se puede representar mediante lista de adyacencia o matriz de adyacencia.
- El grado de un vértice es la cantidad de aristas que lo conectan.
- Pueden contener ciclos (caminos cerrados).
- Pueden ser conexos (todos los vértices están conectados entre sí) o no conexos.
- Se utilizan en problemas como redes sociales, conexiones físicas (como redes eléctricas), rutas no orientadas, etc.

Los recorridos como DFS (Depth-First Search) y BFS (Breadth-First Search) permiten explorar el grafo para descubrir sus propiedades, 
como componentes conexas, ciclos, caminos entre nodos, etc.
"""

from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_Vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def agregar_arista(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if v2 not in self.vertices[v1]:
                self.vertices[v1].append(v2)
            if v1 not in self.vertices[v2]:
                self.vertices[v2].append(v1)
        else:
            print("Arista o Aristas no encontradas")

    def mostrar_grafo(self):
        for vertice in self.vertices:
            print(f"{vertice} -> {self.vertices[vertice]}")
    
    def grado(self, v) -> int:
        if v not in self.vertices:
            return None
        return len(self.vertices[v])
    
    def eliminarVertice(self, v):
        if v in self.vertices:
            
            #Iteramos sobre los elementos para eliminar la doble direccion
            for item in self.vertices[v]:
                self.vertices[item].remove(v)
            del self.vertices[v]
    
    def eliminarArista(self, v1, v2):
        if self.existeCamino(v1,v2):
            self.vertices[v1].remove(v2)
            self.vertices[v2].remove(v1)
    
    def existeCamino(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            for element in self.vertices[v1]:
                if element == v2:
                    return True
            return False
        return False       
    
    def dfs(self, inicio):
        visitados = set()
        self.__dfsRecursivo(inicio, visitados)
        print()
        
    def __dfsRecursivo(self, actual, visitados):
        if actual not in visitados:
            print(actual, end=" - ")  #Esta es la accion de visitar al nodo
            visitados.add(actual)
            
        for vecino in self.vertices[actual]:
            if vecino not in visitados:
                self.__dfsRecursivo(vecino, visitados)
        
        
    def bfs(self, inicio):
        if inicio not in self.vertices:
            return
        
        visitados = set()
        cola = deque()
        
        cola.append(inicio)
        visitados.add(inicio)
        
        while cola:
            actual = cola.popleft()
            print(actual, end=" - ")
            
            for vecino in self.vertices[actual]:
                if vecino not in visitados:
                    cola.append(vecino)
                    visitados.add(vecino)
        print()
    
    # DEPTH FIRST SEARCH SIN IMPRIMIR ------------------------------------------
    # def __dfs2(self, inicio):
    #     visitados = set()
    #     self.__DFS2Recursivo(inicio, visitados)
    
    def __DFS2Recursivo(self, actual, visitados:set):
        if actual not in visitados:
            visitados.add(actual)
        
        for vecino in self.vertices[actual]:
            if vecino not in visitados:
                self.__DFS2Recursivo(vecino, visitados)
    #-------------------------------------------------------------------        
    def esConexo(self):
        
        visitados = set()
        #Nodo inicio el next sirve opara
        #self.vertices es un diccionario, donde las keys son los nodos (vértices) del grafo.
        # iter(self.vertices) crea un iterador sobre esas keys (los vértices).
        # next(...) toma el primer elemento de ese iterador. Es decir, un vértice cualquiera (el primero que encuentra Python internament
        nodo_inicio = next(iter(self.vertices))
        self.__DFS2Recursivo(nodo_inicio, visitados)
        
        return len(visitados) == len(self.vertices)
        
        
grafito = Grafo()

grafito.agregar_Vertice("A")
grafito.agregar_Vertice("B")
grafito.agregar_Vertice("C")
grafito.agregar_Vertice("D")
grafito.agregar_Vertice("E")
grafito.agregar_Vertice("F")
grafito.agregar_Vertice("G")
grafito.agregar_Vertice("H")



grafito.agregar_arista("A", "B")
grafito.agregar_arista("A", "D")
grafito.agregar_arista("A", "E")
grafito.agregar_arista("B", "D")
grafito.agregar_arista("B", "C")
grafito.agregar_arista("D", "G")
grafito.agregar_arista("D", "F")
grafito.agregar_arista("F", "G")
grafito.agregar_arista("F", "H")

grafito.mostrar_grafo()

grafito.mostrar_grafo()
# gradoA = grafito.grado("A")
# print(gradoA)

# print(grafito.existeCamino("A", "O"))
print("DFS-------------------")
grafito.dfs("A")
print("BFS-------------------")
grafito.bfs("A")