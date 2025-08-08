from collections import deque

class GrafoD:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, data):
        if data not in self.vertices:
            self.vertices[data] = []
    
    def agregarArista(self, v1, v2):
        """Agrega direccion desde el v1 hasta el v2"""
        if v1 not in self.vertices and v2 not in self.vertices:
            return
        if v2 not in self.vertices[v1]:
            self.vertices[v1].append(v2)
    
    def mostrarGrafo(self):
        for item in self.vertices:
            print(f"{item} : {self.vertices[item]}")

    def existeArista(self, v1, v2) -> bool:
        if v1 and v2 in self.vertices:
            if v2 in self.vertices[v1]:
                return True
        return False
    
    def existeVertice(self, v) -> bool:
        return v in self.vertices
    
    def eliminarVertice(self, v):
        if self.existeVertice(v):
            del self.vertices[v]
            for item in self.vertices:
                if v in self.vertices[item]:
                    self.vertices[item].remove(v)
    
    def eliminarAista(self, v1, v2):
        if self.existeArista(v1, v2):
            self.vertices[v1].remove(v2)
      
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
        print("")

            
    def DFS(self, inicio):
        if inicio not in self.vertices:
            return
       
        visitados = set() 
        self.__DFSRecursivo(inicio, visitados)
        print()
        
    def __DFSRecursivo(self, actual, visitados: set):
        if actual not in visitados:
            print(actual, end=" ")
            visitados.add(actual)
        
        for vecino in self.vertices[actual]:
            if vecino not in visitados:
                self.__DFSRecursivo(vecino, visitados)
          
grafito = GrafoD()


grafito.agregarVertice("A")
grafito.agregarVertice("B")
grafito.agregarVertice("C")
grafito.agregarVertice("D")

grafito.agregarArista("A", "B")
grafito.agregarArista("B", "C")
grafito.agregarArista("D", "C")
grafito.agregarArista("B", "D")

print(grafito.existeArista("C", "D"))

grafito.mostrarGrafo()
print("---------------")
# grafito.eliminarVertice("B")
# grafito.eliminarAista("B", "C")
grafito.mostrarGrafo()

grafito.bfs("B")
grafito.DFS("A")