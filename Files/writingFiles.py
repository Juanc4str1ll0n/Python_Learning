#Python writing diles (.txt .json .csv)

text = "I like pizza ! "
filePath = 'Prueba.txt'   #Si no se pone una ruta completa se crea en el mismo directorio del programa. 

#Funcion open en python:
# Esta es una función incorporada de Python que se usa para abrir archivos.

# Puede abrir archivos en diferentes modos como:
# "r" = leer (read)
# "w" = escribir (write) → si ya existe, lo sobrescribe
# "a" = agregar (append) → si ya existe, añade al final
# "x" = crear → da error si ya existe
# "rb", "wb" = modo binario

with open( file=filePath , mode="w") as file :
    file.write(text)
    print(f"Archive '{filePath}' was created!")