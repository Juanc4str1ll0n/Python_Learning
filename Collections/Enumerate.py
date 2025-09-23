"""
==========================================
 APUNTES SOBRE EL MÉTODO enumerate EN PYTHON
==========================================

📌 ¿Qué es enumerate?
----------------------
- Es una función incorporada (built-in) de Python.
- Se usa principalmente en los bucles (for).
- Permite iterar sobre una secuencia (lista, tupla, string, etc.)
  obteniendo al mismo tiempo el índice y el valor del elemento.

📌 Sintaxis:
------------
    enumerate(iterable, start=0)

- iterable → cualquier objeto iterable (lista, tupla, string, etc.)
- start    → índice inicial (por defecto es 0, pero se puede cambiar).

📌 ¿Qué devuelve?
-----------------
Devuelve un objeto de tipo "enumerate", que genera tuplas con la forma:
    (indice, elemento)

Ejemplo: enumerate(["a","b","c"]) → (0,"a"), (1,"b"), (2,"c")

"""

# =============================
# EJEMPLOS BÁSICOS DE enumerate
# =============================

# Ejemplo 1: recorrer una lista
frutas = ["manzana", "pera", "naranja", "uva"]

print("Ejemplo 1: Iterar lista con índices")
for indice, valor in enumerate(frutas):
    print(indice, valor)

# ------------------------------------------

# Ejemplo 2: usando start para cambiar el índice inicial
print("\nEjemplo 2: Iniciar índice desde 1")
for indice, valor in enumerate(frutas, start=1):
    print(indice, valor)

# ------------------------------------------

# Ejemplo 3: con cadenas de texto
print("\nEjemplo 3: Enumerar caracteres de un string")
for indice, letra in enumerate("Python"):
    print(f"Letra {letra} en posición {indice}")

# ------------------------------------------

# Ejemplo 4: convertir el objeto enumerate a lista/tupla
print("\nEjemplo 4: Convertir enumerate en lista de tuplas")
resultado = list(enumerate(frutas))
print(resultado)  # [(0, 'manzana'), (1, 'pera'), (2, 'naranja'), (3, 'uva')]

# ------------------------------------------

# Ejemplo 5: Usar enumerate para actualizar valores en una lista
print("\nEjemplo 5: Actualizar lista con índices")
numeros = [10, 20, 30, 40]
for i, valor in enumerate(numeros):
    numeros[i] = valor * 2
print(numeros)  # [20, 40, 60, 80]

# ------------------------------------------

# Ejemplo 6: enumerate con condiciones
print("\nEjemplo 6: Buscar elementos con enumerate")
for indice, fruta in enumerate(frutas):
    if fruta == "naranja":
        print(f"Encontrada '{fruta}' en la posición {indice}")

"""
📌 Resumen:
-----------
- enumerate evita tener que usar range(len(iterable)).
- Hace el código más limpio y legible.
- Muy útil cuando necesitas índice + valor en un bucle.

Ejemplo tradicional vs. con enumerate:
--------------------------------------
    # Forma tradicional
    for i in range(len(frutas)):
        print(i, frutas[i])

    # Con enumerate
    for i, fruta in enumerate(frutas):
        print(i, fruta)
"""
