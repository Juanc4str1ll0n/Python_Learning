string1 = "Hola a todos"
string2 = "Como estan"

concatenacion = "".join(string1)
concatenacion2 = "".join([string1, string2])

print(concatenacion)
print(concatenacion2)

#--------------------------------------------
#FORMAT 
nombre = 'Juan'
edad = 90

mensaje = 'Hola a {} como tiene {}'.format(nombre, edad)

print(mensaje)

#-------------------------------
#Strip
#Elimina espacios al inicio y al final de una cadena
cadena = "   Juanito Juan     "

print(cadena.strip())

#Manejo de subcadenas

cadenita = "Adios mundo"

print(cadenita[0:5]) #Desde el indice 0 hasta el 4 porque no se toma el 5
print(cadenita[::-1])

#--------------------------------
#METODO REPLACE
cadenota = "Hola a todos"

print(cadenota.replace("Hola", "Adios")) #Reemplaza lo que le indique por adios, si no existe el primer parametro devuelve la cadena normal

#-----------------------------------------
# Metodo Split para separar cadenas

mi_cadena = "Juan, Pedro, Martin"
lista = mi_cadena.split(",")  #-> En este caso mi caracter separador va a ser la coma ,
print(lista)

