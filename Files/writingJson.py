import json

# Diccionario que vamos a guardar
data = {
    "nombre": "Juan",
    "edad": 25,
    "hobbies": ["leer", "jugar fútbol", "programar"],
    "carrera" : "Ingenieria de sistemas y computacion"
}

# Nombre del archivo a guardar y su ruta, en este caso en la carpeta
filePath = 'Files/datos.json'

# Escribir el archivo JSON
#La opcion json.dump me va a convertir el diccionario a formato Json y ademas
#   Convierte un objeto de Python (como un diccionario o una lista)
#    A texto en formato JSON (ej: con comillas dobles, llaves, corchetes, etc.)
# Y lo escribe directamente en un archivo

with open(filePath, "w") as file:
    json.dump(data, file, indent=4)
    print(f"Archivo '{filePath}' fue creado exitosamente.")
