import json

datos = {
    "Squidward":31,
    "Spongebob": 17,
    "Patrick":20
}

path = 'Files/escritura2.json'

with open(path, 'w') as file:
    json.dump(datos, file)
    print("Se hizo con exito esta mierda")
