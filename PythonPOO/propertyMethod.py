# El decorador @property permite que un método se comporte como si fuera un atributo.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Nota el guion bajo: convención de "privado"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

# Uso
c = Circle(5)
print(c.radius)     # 5  (usa el getter)
print(c.area)       # 78.5  (área calculada)

c.radius = 10       # usa el setter
print(c.area)       # 314.0

# c.radius = -2    # Esto lanzaría un error
