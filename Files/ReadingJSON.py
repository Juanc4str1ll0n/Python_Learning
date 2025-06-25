import json
file_path = "Files/datos.json"

#USAMOS R PARA READ, GUARDAMOS EN UNA VARIABLE CONTENIDO FILE.READ
try:
    with open(file_path, "r") as file:
        contenido = json.load(file)
        print(contenido)
        print(contenido["edad"])
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permiso de leer este archivo")