#En un arbol binario se encuentra la raiz

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BinaryTree:
    def __init__(self):
        self.raiz = None
        self.size = 0
    
    def insertar(self, valor):
        if self.raiz == None:
            self.raiz = Node(valor)
            self.size += 1
        else:
            self._insertarRecursivo(Nodo_actual = self.raiz, valor =valor)   #Empezamos desde la raiz

    
    def _insertarRecursivo(self, Nodo_actual, valor):
        
        #Insertar a la izquierda (Es menor)
        if valor < Nodo_actual.valor:
            if Nodo_actual.izquierdo == None:
                Nodo_actual.izquierdo = Node(valor)
                self.size += 1
                return
            else:
                self._insertarRecursivo(Nodo_actual= Nodo_actual.izquierdo, valor= valor)
        
        #Insertar a la derecha (Es mayor)
        elif valor > Nodo_actual.valor:
            if Nodo_actual.derecho == None:
                Nodo_actual.derecho = Node(valor)
                self.size += 1
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

    def Peso(self):
        return self.size
    
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
        print()
        
    def _inordenRecursivo(self, nodo):
        if nodo is not None:
            self._inordenRecursivo(nodo.izquierdo)
            print(nodo.valor, end=" - ")
            self._inordenRecursivo(nodo.derecho)
        
        
    def preorden(self):
        #Raiz - izq  - derecha
        self._preordenRecursivo(self.raiz)
        print()
    
    def _preordenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor, "-",  end=" ")
            self._preordenRecursivo(nodo.izquierdo)
            self._preordenRecursivo(nodo.derecho)
            
    def postorden(self):
        self._postordenRecursivo(self.raiz)
        print()
        
    def _postordenRecursivo(self, nodo):
        if nodo is not None:
            self._postordenRecursivo(nodo.izquierdo)
            self._postordenRecursivo(nodo.derecho)
            print(nodo.valor, end=" - ")
            
    def contarNodos(self):
        return self.size
    
    def altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if nodo == None:
            return 0
        
        izquierdo = self._altura_recursiva(nodo.izquierdo) 
        derecho = self._altura_recursiva(nodo.derecho)

        return 1 + max(izquierdo, derecho) 
    
    def es_balanceado(self):
        return self._es_balanceado_recursivo(self.raiz)
    
    def _es_balanceado_recursivo(self, nodo):
        if nodo is None:
            return True
        
        altura_izquierda = self._altura_recursiva(nodo.izquierdo)
        altura_derecha = self._altura_recursiva(nodo.derecho)
        
        diferencia = abs(altura_izquierda - altura_derecha)
        
        return (diferencia <= 1 and self._es_balanceado_recursivo(nodo.izquierdo) and self._es_balanceado_recursivo(nodo.derecho))
    
    def aListaOrdenada(self):
        return self._aListaOrdenada(self.raiz)

    def _aListaOrdenada(self, nodo):
        if nodo is None:
            return []

        izquierda = self._aListaOrdenada(nodo.izquierdo)
        centro = [nodo.valor]
        derecha = self._aListaOrdenada(nodo.derecho)

        return izquierda + centro + derecha

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
        #Actualizamos la raiz si es necesario con la llamada recursiva a eliminar desde la raiz un cierto valor.
        
    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
            #Actualizamos el izquierdo con recursividad si es menor
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
            #Actualizamos derecho con recursividad si es mayor
            
        else:
            # Nodo encontrado
            if nodo.izquierdo is None and nodo.derecho is None:
                return None  # caso 1: hoja
            elif nodo.izquierdo is None:
                return nodo.derecho  # caso 2: un hijo derecho
            elif nodo.derecho is None:
                return nodo.izquierdo  # caso 2: un hijo izquierdo
            else:
                # caso 3: dos hijos
                sucesor = self._minimo(nodo.derecho)
                nodo.valor = sucesor.valor
                nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        return nodo


    def _minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

        
    
arbolito = BinaryTree()

arbolito.insertar(50)
arbolito.insertar(40)
arbolito.insertar(30)
arbolito.insertar(31)
arbolito.insertar(20)
arbolito.insertar(45)
arbolito.insertar(42)
arbolito.insertar(70)
arbolito.insertar(69)
arbolito.insertar(90)

print(arbolito.buscar(90))

arbolito.inorden()
arbolito.preorden()
arbolito.postorden()

# print(arbolito.altura())

# print(arbolito.contarNodos())

# print(arbolito.altura())
print(arbolito.es_balanceado())

listaArbolito = arbolito.aListaOrdenada()
print(listaArbolito)

arbolito.eliminar(90)
print("--------------")
arbolito.inorden()