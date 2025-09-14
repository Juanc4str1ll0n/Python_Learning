#Triangulo equilatero
num = int(input("Proporcione el numero de filas"))

for i in range(num + 1):
    espacios = ' '*(num - i)
    estrellas = '*'*(2 * i-1 )
    print(espacios, estrellas)
    
#Triangulo lado derecho
print("-----------------------------------")
for i in range(num + 1):
    estrellas = '*'*(i)
    print(espacios, estrellas)

#Triangulo lado izquierdo 
print("-----------------------------------")
for i in range(num + 1):
    espacios = ' '*(num - i)
    estrellas = '*'*(i)
    print(espacios, estrellas)

#Rombo
print("-----------------------------------")

# Triángulo de arriba (incluye el centro)
for i in range(1, num + 1):
    espacios = ' ' * (num - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas)

# Triángulo de abajo (sin repetir el centro)
for i in range(num - 1, 0, -1):
    espacios = ' ' * (num - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas)

