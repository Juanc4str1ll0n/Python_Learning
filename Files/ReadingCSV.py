import csv

file_Path = "Files/prueba2.csv"

try:
    with open(file_Path, "r") as file:
        contenido = csv.reader(file)
        for linea in contenido:
            print(linea)
            # print(linea[1]) -> aqui imprimiria una linea en especifico del archivo csv si la necesito
        print("Exito en leer!")
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permiso de leer este archivo")