# -----------------------------------------
# Uso de 'global' en Python
# -----------------------------------------

x = 10  # variable global

def solo_leer():
    # Podemos LEER una variable global sin problema
    print("[solo_leer] x =", x)

def crear_local():
    # Aquí parece que usamos la global,
    # pero en realidad creamos una NUEVA variable local
    x = 20
    print("[crear_local] x =", x)

def modificar_global():
    # Avisamos a Python que queremos la variable global
    global x
    x = 30  # esto sí cambia la global
    print("[modificar_global] x =", x)


print("Valor inicial de x (global):", x)
print("-" * 40)

solo_leer()
print("Después de solo_leer, x global sigue siendo:", x)
print("-" * 40)

crear_local()
print("Después de crear_local, x global sigue siendo:", x)
print("-" * 40)

modificar_global()
print("Después de modificar_global, x global AHORA es:", x)
print("-" * 40)
