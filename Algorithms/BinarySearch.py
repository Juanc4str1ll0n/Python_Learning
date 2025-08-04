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

lista = []
for i in range(1000000):
    lista.append(i)

Start = time.time()   #Midiendo el tiempo
print(binarySearch(lista, 999999))
End = time.time()    #Midiendo el tiempo

print(End - Start)
