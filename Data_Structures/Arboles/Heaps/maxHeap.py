class maxHeap:
    def __init__(self):
        self.heap = []
        
    def insertar(self, data):
        self.heap.append(data)
        self._subir(len(self.heap) -1 )  #Subir el ultimo elemento del heap si es necesario
        
    def _subir(self, indice):
        
        while indice>0:
            padre = (indice -1 ) //2
            if self.heap[indice] > self.heap[padre]:
                self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
                indice = padre
            else:
                break
            
    def eliminarMax(self):
        if len(self.heap) == 0:
            return None
        
        maximo = self.heap[0]
        ultimo = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = ultimo
            self._bajar(0)
            
        return maximo
    
    def _bajar(self, indice):
        size = len(self.heap)
        mayor = indice 
        
        while True:
            izquierdo = 2*indice + 1
            derecho =  2*indice + 2
            
            #Comparar con izquierdo
            if izquierdo < size and self.heap[izquierdo] > self.heap[mayor]:
                mayor = izquierdo
                
            #Comparar con derecho
            if derecho < size and self.heap[derecho] > self.heap[mayor]:
                mayor = derecho
                 
            if mayor != indice:
                self.heap[mayor], self.heap[indice] = self.heap[indice ], self.heap[mayor]
                indice = mayor           
            
            else:
                break
            
    def print(self):
        print(self.heap)
        
    def isEmpty(self):
        return len(self.heap) == 0
    
    def size(self) -> int :
        return len(self.heap)
    

ejemplo = maxHeap()

# ejemplo.insertar(100)
ejemplo.insertar(90)
ejemplo.insertar(80)
ejemplo.insertar(65)
ejemplo.insertar(75)
ejemplo.insertar(9)
ejemplo.insertar(120)

ejemplo.print()