"""
APUNTES DE SETS (CONJUNTOS) EN PYTHON
-------------------------------------

Un SET es una colección desordenada, que no admite elementos duplicados.
Se define usando llaves {} o con la función set().

Características:
✔️ No mantiene un orden específico (los elementos pueden cambiar de posición al imprimir).
✔️ No permite duplicados.
✔️ Es mutable (se pueden agregar o eliminar elementos).
✔️ Se usa mucho para operaciones matemáticas de conjuntos.
"""

# Crear sets
set_vacio = set()  # Importante: {} crea un diccionario, no un set
set_numeros = {1, 2, 3, 4, 5}
set_mixto = {10, "Python", True, 3.14, 10}  # el 10 duplicado será eliminado

print("Set vacío:", set_vacio)
print("Set de números:", set_numeros)
print("Set mixto (sin duplicados):", set_mixto)

# No se accede por índice (porque no tienen orden)
# print(set_numeros[0])  # ❌ Esto da error

# MÉTODOS DE LOS SETS
print("\n--- MÉTODOS DE SETS ---")

# 1. add(): Agregar un elemento
set_numeros.add(6)
print("add:", set_numeros)

# 2. update(): Agregar múltiples elementos
set_numeros.update([7, 8, 9])
print("update:", set_numeros)

# 3. remove(): Eliminar un elemento (error si no existe)
set_numeros.remove(9)
print("remove:", set_numeros)

# 4. discard(): Eliminar un elemento (sin error si no existe)
set_numeros.discard(100)  # no genera error
print("discard:", set_numeros)

# 5. pop(): Elimina y devuelve un elemento aleatorio
eliminado = set_numeros.pop()
print("pop (elemento eliminado):", eliminado)
print("Set después de pop:", set_numeros)

# 6. clear(): Vacía el conjunto
temp = {1, 2, 3}
temp.clear()
print("clear:", temp)

# OPERACIONES DE CONJUNTOS
print("\n--- OPERACIONES ENTRE SETS ---")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

# Unión (todos los elementos sin repetir)
print("Unión A | B:", A | B)
print("A.union(B):", A.union(B))

# Intersección (solo los comunes)
print("Intersección A & B:", A & B)
print("A.intersection(B):", A.intersection(B))

# Diferencia (elementos de A que no están en B)
print("Diferencia A - B:", A - B)
print("A.difference(B):", A.difference(B))

# Diferencia simétrica (elementos que están en A o B, pero no en ambos)
print("Diferencia simétrica A ^ B:", A ^ B)
print("A.symmetric_difference(B):", A.symmetric_difference(B))

# OTROS MÉTODOS ÚTILES
print("\n--- OTROS MÉTODOS ---")
C = {1, 2}
D = {1, 2, 3, 4}

print("C es subconjunto de D:", C.issubset(D))   # True
print("D es superconjunto de C:", D.issuperset(C))  # True
print("C y B son disjuntos:", C.isdisjoint({5, 6}))  # True

# CONGELAR SETS (INMUTABLES)
print("\n--- FROZENSET ---")
# Un frozenset es un conjunto inmutable (no permite añadir ni eliminar elementos)
fs = frozenset([1, 2, 3, 3, 4])
print("frozenset:", fs)
# fs.add(5)  # ❌ Da error porque es inmutable

"""
RESUMEN
-------
Sets (conjuntos):
✔️ Colecciones sin orden y sin duplicados
✔️ Métodos: add, update, remove, discard, pop, clear
✔️ Operaciones matemáticas: unión, intersección, diferencia, diferencia simétrica
✔️ Métodos de relación: issubset, issuperset, isdisjoint
✔️ frozenset -> versión inmutable
"""
