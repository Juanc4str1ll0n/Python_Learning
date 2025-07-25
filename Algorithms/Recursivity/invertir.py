#Invertir cadenas y contar cuantas letras hay en una palabra
def invertir(cadena):
    if cadena == "":
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]
    
print(invertir("Hola"))


def contarLetras(cadena):
    if cadena == "":
        return 0
    else:
        return contarLetras(cadena[1:]) + 1

print(contarLetras("Hola"))


