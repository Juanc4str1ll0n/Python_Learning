class MinHeap:
    def __init__(self):
        self.heap = []  #Aqui se guarda el heap
        
    def insertar(self, valor):
        self.heap.append(valor)   #Paso 1: Lo ponemos al final
        self._subir(len(self.heap) - 1)  #Paso 2: Lo subimos si es necesario
        
    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2   #Aplicamos la formula
            if self.heap[indice] < self.heap[padre]:
                self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
                indice = padre
            else:
                break
    
    #Metodo para eliminar la raiz y retornarla
    def eliminarMin(self):
        
        #Si el heap esta vacio
        if len(self.heap) == 0:
            return None
        
        minimo = self.heap[0]    #Guardamos el primer valor para retornar
        ultimo = self.heap.pop()  #El ultimo
        
        if len(self.heap) > 0:
            self.heap[0] = ultimo
            self._bajar(0)
        
        return minimo
    
    def _bajar(self, indice):
        size = len(self.heap)
        menor = indice            #La variable menor es la que Vamos a intercambiar
        
        while True:       #Bucle para iterar hasta que se baje donde es
            izquierda = 2 * indice + 1       #Hijo izquierdo del indice
            derecha = 2 * indice + 2         #Hijo derecho del indice 
             
            if izquierda < size and self.heap[izquierda] < self.heap[menor]:   #Comparamos el menor con su hijo izquierdo
                menor = izquierda
                
            if derecha < size and self.heap[derecha] < self.heap[menor]:       #Comparamos con el hijo derecho para ver el menor de los 3 
                menor = derecha
            
            if menor != indice:        #Si el menor se cambio de lugar
                self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice] 
                 
            else:   #Ya esta en su lugar
                break
    
    def getList(self) -> list:
        
        if len(self.heap) == 0:
            return []
        
        return self.heap
    
    def obtenerMin(self):
        
        if len(self.heap) == 0:
            return None
        
        return self.heap[0]
    
    def size(self) -> int :
        
        return len(self.heap)
    
    def estaVacio(self):
        return len(self.heap) == 0
    
    
def heapSort(lista):
    heap = MinHeap()  # Usamos la clase para implementar un algoritmo de ordenamiento

    # Paso 1: Insertar todo en el heap
    for elemento in lista:
        heap.insertar(elemento)

    # Paso 2: Extraer ordenadamente
    resultado = []
    while not heap.estaVacio():
        resultado.append(heap.eliminarMin())
    
    return resultado
    
    
lista = [5, 3, 8, 1, 2]


mini = MinHeap()

mini.insertar(5)
mini.insertar(3)
mini.insertar(8)
mini.insertar(1)
mini.insertar(2)

print(mini.heap)