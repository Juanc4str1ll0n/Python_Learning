#Estructura de datos basada en un arbol binario completo, cada nodo tiene sus dos hijos izquierdo y derecho
#Un heap se almacena en un arreglo plano
#Sus formulas son como i como indice:
# 2i +1 -> Hijo izquierdo ||   2i+2 -> Hijo derecho   ||   (i-1) //2 padre de i

heap = [1, 2, 3, 4, 5, 6]

i = 2  #-> Indice 2 del heap(3)

print(heap[2*i + 1])  #Hijo izquierdo de 3 -> (6)

# print(heap[2*i + 2])   #Hijo derecho de 3  -> No existe, se pasa

i = 0  #-> Indice 0
print(heap[2*i + 2])  #Hijo derecho de la raiz 1   ->3
