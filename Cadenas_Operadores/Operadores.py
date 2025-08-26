
#Asignacion multiple

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

#Asignacion encadenada

k = v = b = 100

print(k)
print(v)
print(b)

#Intercambio de variables

x, y = 10, 20
print(x, y )

x,y = y, x
print(x, y)

#Recibir multiples valores de la entrada del usuario

nombres, apellidos = input("Ingresa tu nombre y apellido separado por coma: ").split(",")

print(f"nombres: {nombres}, apellidos:{apellidos}")