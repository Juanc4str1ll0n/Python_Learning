"""
==================================================
📘 APUNTES SOBRE DICCIONARIOS EN PYTHON
==================================================
Un diccionario es una colección de pares clave:valor.
- Las claves son únicas e inmutables (str, int, tuple…).
- Los valores pueden ser de cualquier tipo.
- Los diccionarios son MUTABLES.

Sintaxis:
    diccionario = {
        "clave1": "valor1",
        "clave2": "valor2"
    }
"""

# -------------------------------------------------
# Crear un diccionario
# -------------------------------------------------
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}
print("Diccionario inicial:", persona)

# -------------------------------------------------
# Acceso a valores
# -------------------------------------------------
print("Nombre:", persona["nombre"])  # acceso directo
print("Edad con get():", persona.get("edad"))
print("Altura con get():", persona.get("altura", "No existe"))  # valor por defecto

# -------------------------------------------------
# Modificar y agregar elementos
# -------------------------------------------------
persona["edad"] = 26                  # Modificar
persona["profesion"] = "Ingeniero"    # Agregar nuevo
print("Diccionario modificado:", persona)

# -------------------------------------------------
# Eliminar elementos
# -------------------------------------------------
persona.pop("ciudad")      # elimina por clave
print("Después de pop:", persona)

persona.popitem()          # elimina el último par clave:valor
print("Después de popitem:", persona)

# del persona["edad"]      # elimina por clave
# persona.clear()          # elimina todo

# -------------------------------------------------
# Recorrer un diccionario
# -------------------------------------------------
persona = {"nombre": "Ana", "edad": 30, "pais": "Colombia"}

print("\nRecorrer claves:")
for clave in persona:
    print(clave)

print("\nRecorrer claves con .keys():")
for clave in persona.keys():
    print(clave)

print("\nRecorrer valores con .values():")
for valor in persona.values():
    print(valor)

print("\nRecorrer clave y valor con .items():")
for clave, valor in persona.items():
    print(clave, "→", valor)

# -------------------------------------------------
# Métodos importantes de los diccionarios
# -------------------------------------------------

# .get()
print("\n.get():", persona.get("edad"))  # 30

# .keys()
print(".keys():", persona.keys())

# .values()
print(".values():", persona.values())

# .items()
print(".items():", persona.items())

# .update()
persona.update({"edad": 35})
print("\n.update():", persona)

# .pop()
valor_eliminado = persona.pop("pais")
print(".pop(): eliminó", valor_eliminado, "→", persona)

# .popitem()
clave_valor = persona.popitem()
print(".popitem(): eliminó", clave_valor, "→", persona)

# .copy()
copia = persona.copy()
print(".copy():", copia)

# .fromkeys()
nuevo_dic = dict.fromkeys(["a", "b", "c"], 0)
print(".fromkeys():", nuevo_dic)

# .setdefault()
persona.setdefault("ciudad", "Medellín")
print(".setdefault():", persona)

"""
==================================================
RESUMEN
==================================================
- Diccionarios = colección mutable de pares clave:valor.
- Métodos principales:
    get(), keys(), values(), items(), update(), pop(),
    popitem(), clear(), copy(), fromkeys(), setdefault()
- Útiles para representar objetos, almacenar configuraciones,
  y trabajar con datos en formato JSON.
==================================================
"""
