from random import randint
#Generador de email

nombre = input("Ingresa tu nombre: ")
empresa =input("Ingresa el nombre de la empresa: ")
ext = input("Ingresa la extension del dominio: ")

#Juan David Castrillon
nombre_normalizado = nombre.lower().replace(" ", ".")

print(f"{nombre_normalizado}@{empresa}{ext}")

#Generador de id unico 

print("\nBienvenido al generador de id unico")

nombre2 = input("Ingresa tu nombre:  ")
apellido2 = input("Ingresa tu apellido:  ")
ano = input("Ingresa tu ano de nacimiento:  ")
r = randint(1000, 10000)

nombres = nombre2[0:2].upper()
apellidos = apellido2[0:2].upper()

anos = ano[-2:]

print(f"{nombre2}{apellidos}{anos}{r}")