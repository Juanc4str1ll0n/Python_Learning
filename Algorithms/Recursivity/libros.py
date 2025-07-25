#Contar las paginas de un libro mediante recursividad

def totalPaginas(libros:list) -> int:
    if len(libros) == 1:
        return libros[0]
    
    return libros[0] + totalPaginas(libros[1:])

libros = [100,200,300,400,500]

print(totalPaginas(libros))