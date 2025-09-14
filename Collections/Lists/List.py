"""
APUNTES DE LISTAS EN PYTHON
---------------------------

Una LISTA en Python es una estructura de datos que nos permite almacenar varios elementos 
en una sola variable. Los elementos pueden ser de cualquier tipo (números, cadenas, booleanos, etc.).

Las listas se definen usando CORCHETES [] y sus elementos están separados por comas.
"""

# Crear listas
lista_vacia = []  # Lista sin elementos
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [10, "Python", True, 3.14]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("\n--- Acceso a elementos ---")
print("Primer elemento:", lista_numeros[0])   # Índices comienzan en 0
print("Último elemento:", lista_numeros[-1]) # Índices negativos cuentan desde el final
print("Sublista:", lista_numeros[1:4])       # Slice -> [2, 3, 4]

# Modificar elementos
lista_numeros[0] = 100
print("Lista modificada:", lista_numeros)

# MÉTODOS DE LAS LISTAS
print("\n--- MÉTODOS DE LISTAS ---")

# 1. append(): Agregar un elemento al final
lista = [1, 2, 3]
lista.append(4)
print("append:", lista)

# 2. insert(): Insertar un elemento en un índice específico
lista.insert(1, "nuevo")
print("insert:", lista)

# 3. extend(): Agregar múltiples elementos (otra lista) al final
lista.extend([5, 6, 7])
print("extend:", lista)

# 4. remove(): Eliminar el primer elemento con el valor especificado
lista.remove("nuevo")
print("remove:", lista)

# 5. pop(): Eliminar un elemento por su índice (por defecto el último)
ultimo = lista.pop()
print("pop (eliminado):", ultimo)
print("lista después de pop:", lista)

# 6. index(): Obtener el índice de un valor
print("index del número 2:", lista.index(2))

# 7. count(): Contar cuántas veces aparece un valor
print("count del número 2:", lista.count(2))

# 8. sort(): Ordenar la lista (solo funciona con datos comparables)
lista_numeros = [3, 1, 4, 2]
lista_numeros.sort()
print("sort ascendente:", lista_numeros)

lista_numeros.sort(reverse=True)
print("sort descendente:", lista_numeros)

# 9. reverse(): Invierte el orden de los elementos
lista = [1, 2, 3, 4]
lista.reverse()
print("reverse:", lista)

# 10. copy(): Crea una copia de la lista
copia = lista.copy()
print("copy:", copia)

# 11. clear(): Vacía la lista
lista.clear()
print("clear:", lista)

# FUNCIONES ÚTILES CON LISTAS
print("\n--- FUNCIONES ÚTILES ---")
nums = [10, 20, 30, 40, 50]

print("len():", len(nums))       # Número de elementos
print("max():", max(nums))       # Valor máximo
print("min():", min(nums))       # Valor mínimo
print("sum():", sum(nums))       # Suma de los elementos
print("sorted():", sorted(nums)) # Retorna una lista ordenada sin modificar la original

# LISTAS POR COMPRENSIÓN
print("\n--- LISTAS POR COMPRENSIÓN ---")
# Crear listas de forma compacta con bucles
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)

pares = [x for x in range(10) if x % 2 == 0]
print("Pares:", pares)

"""
RESUMEN
-------
Las listas son colecciones mutables que permiten:
✔️ Almacenar múltiples valores de distintos tipos
✔️ Acceder, modificar y eliminar elementos
✔️ Usar métodos poderosos como append, extend, sort, etc.
✔️ Combinarlas con bucles y condiciones (list comprehensions)

Son una de las estructuras de datos más usadas en Python.
"""
