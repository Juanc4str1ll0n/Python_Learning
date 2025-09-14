"""
APUNTES DE TUPLAS EN PYTHON
---------------------------

Una TUPLA en Python es una colección ordenada, similar a las listas, 
pero INMUTABLE (no se puede modificar después de ser creada).

Se definen con paréntesis () y los elementos separados por comas.
"""

# Crear tuplas
tupla_vacia = ()  # Tupla vacía
tupla_un_elemento = (5,)  # Si tiene solo 1 elemento, se necesita la coma
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = (10, "Python", True, 3.14)

print("Tupla vacía:", tupla_vacia)
print("Tupla de un solo elemento:", tupla_un_elemento)
print("Tupla de números:", tupla_numeros)
print("Tupla mixta:", tupla_mixta)

# Acceder a elementos
print("\n--- Acceso a elementos ---")
print("Primer elemento:", tupla_numeros[0])   # Índice 0
print("Último elemento:", tupla_numeros[-1]) # Índice negativo
print("Subtupla:", tupla_numeros[1:4])       # Slice -> (2, 3, 4)

# Inmutabilidad
print("\n--- Inmutabilidad ---")
# tupla_numeros[0] = 100  # ❌ Esto daría error
print("Las tuplas no permiten modificación directa.")

# MÉTODOS DISPONIBLES
print("\n--- MÉTODOS DE TUPLAS ---")
# Solo dos métodos principales: count() e index()

tupla = (1, 2, 2, 3, 4, 2, 5)

print("count del número 2:", tupla.count(2))  # Cuenta las veces que aparece 2
print("index del número 3:", tupla.index(3))  # Devuelve el índice de la primera ocurrencia de 3

# FUNCIONES ÚTILES CON TUPLAS
print("\n--- FUNCIONES ÚTILES ---")
nums = (10, 20, 30, 40, 50)

print("len():", len(nums))       # Número de elementos
print("max():", max(nums))       # Valor máximo
print("min():", min(nums))       # Valor mínimo
print("sum():", sum(nums))       # Suma de los elementos
print("sorted():", sorted(nums)) # Retorna lista ORDENADA (no modifica la tupla)

# TUPLAS ANIDADAS
print("\n--- TUPLAS ANIDADAS ---")
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print("Acceder al 2:", tupla_anidada[0][1])  # Segundo elemento de la primera tupla

# DESEMPAQUETADO DE TUPLAS
print("\n--- DESEMPAQUETADO ---")
persona = ("Juan", 25, "Colombia")
nombre, edad, pais = persona
print("Nombre:", nombre)
print("Edad:", edad)
print("País:", pais)

# USO COMO CLAVE EN DICCIONARIOS
print("\n--- USO COMO CLAVE EN DICCIONARIOS ---")
# Como son inmutables, las tuplas pueden ser usadas como claves en diccionarios
dic = { (1, 2): "coordenada A", (3, 4): "coordenada B" }
print(dic)
print("Valor de la clave (1, 2):", dic[(1, 2)])

"""
RESUMEN
-------
Las tuplas son colecciones ordenadas e inmutables:
✔️ No se pueden modificar después de creadas
✔️ Métodos: count() e index()
✔️ Admiten funciones como len, max, min, sum, sorted
✔️ Soportan slicing y anidamiento
✔️ Útiles cuando necesitamos datos que no cambien (constantes, coordenadas, etc.)
✔️ Pueden usarse como claves en diccionarios (a diferencia de listas)
"""
