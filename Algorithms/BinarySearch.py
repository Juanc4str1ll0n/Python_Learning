import time

#Version iterativa
def binarySearch(lista: list, objetivo):
    
    izquierda = 0
    derecha = len(lista) -1
    

    while izquierda <= derecha:
        middle = (izquierda + derecha) // 2
        middle_element = lista[middle]
        
        if middle_element == objetivo:
            return middle_element
        
        #Si el objetivo es menor que el actual en la mitad
        elif objetivo < middle_element:
            derecha = middle - 1
            
        else:
            izquierda = middle + 1
            
    print("Elemento no encontrado")
        
#Version recursiva
def recursiveBinarySearch(lista:list, objetivo):
    return _recursiveBinarySearch(lista, objetivo, 0, len(lista)-1)

def _recursiveBinarySearch(lista:list, objetivo, izq, dere):
    if izq > dere:
        return 
    
    middle = (dere - izq) // 2
    middlePosition = lista[middle]
    
    if objetivo == middlePosition:
        return middlePosition
    
    elif objetivo < middlePosition:
        return recursiveBinarySearch(lista, objetivo, izq, middle - 1)
    
    elif objetivo > middlePosition:
        return recursiveBinarySearch(lista, objetivo, middle +1, dere )



lista = []
for i in range(10000000):
    lista.append(i)

Start = time.time()   #Midiendo el tiempo
print(binarySearch(lista, 9999999))
End = time.time()    #Midiendo el tiempo

print(End - Start)
