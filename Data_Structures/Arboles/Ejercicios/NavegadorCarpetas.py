class Node:
    def __init__(self, nombre, es_archivo = False):
        self.nombre = nombre
        self.es_archivo = es_archivo
        self.hijos = []
        
    def es_carpeta(self):
        return self.tipo == "carpeta"

class arbolArchivos:
    def __init__(self):
        self.raiz = Node("root")
        
    def crearCarpeta(self, ruta, nombre):
        padre = self.__buscar_ruta(ruta)
        if padre is None:
            print("Ruta no encontrada")
            return
        
        if padre.es_archivo:
            print("No se puede crear dentro de un archivo")
            return
        
        nueva = Node(nombre)
        padre.hijos.append(nueva)
        print("Carpeta creada")
    
    def __buscar_ruta(self, ruta: str):
        partes = ruta.strip("/").split("/")  #Genera una lista separando los slash
        actual = self.raiz
        
        for parte in partes:
            encontrado = False
            for hijo in actual.hijos:
                if hijo.nombre == parte and not hijo.es_archivo:
                    actual = hijo
                    encontrado = True
                    break
            if not encontrado:
                return None
        return actual
    
    def mostrar(self):
        pass
    
    def __mostrarRecursivo(self):
        pass
    
    def buscar(self, nombre):
        pass
    
    def __buscarRecursivo(self):
        pass
    
    def eliminar(self, ruta_completa):
        pass
    
    def renombrar(self):
        pass
    
    def mover(self):
        pass
    
    def __navegar_ruta(self):
        pass