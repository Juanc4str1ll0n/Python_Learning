# Los magic methods también llamados métodos especiales o dunder methods, por “double underscore”
#                     son funciones que Python llama automáticamente en ciertas operaciones, como:

# __init__: constructor

# __str__: para impresión amigable con print()

# __repr__: para representación interna útil en debug

# __eq__, __lt__, __add__, etc.: para sobrecargar operadores



class Libro:
    def __init__(self, titulo, autor, paginas, precio):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.precio = precio

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.paginas} páginas, ${self.precio})"

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas}, {self.precio})"

    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor

    def __lt__(self, other):
        return self.precio < other.precio

    def __add__(self, other):
        return self.paginas + other.paginas


l1 = Libro("1984", "George Orwell", 328, 15)
l2 = Libro("Rebelión en la Granja", "George Orwell", 112, 10)
l3 = Libro("1984", "George Orwell", 328, 15)

print(l1)           # __str__
print(repr(l2))     # __repr__

print(l1 == l3)     # True  (usa __eq__)
print(l2 < l1)      # True  (usa __lt__)

total_paginas = l1 + l2  # usa __add__
print(f"Total de páginas combinadas: {total_paginas}")
