import os 

filePath = 'c:/Users/juanc/OneDrive/Documents/Universidad/PythonLearning'


#Metodo os.path.exits   --> verifica si un path existe
if os.path.exists(filePath):
    print(f"The path '{filePath}'exist! ")

    #Metodo os.path.isfile --> devuelve true or false si ese path corresponde a un archivo
    if os.path.isfile(filePath):
        print("The file is a path")

    #Metodo os.path.isdir --> devuelve true or false si ese path corresponde a un directorio
    elif os.path.isdir(filePath):
        print("That is a directory")
else:
    print("That does not exist")
