#Greek word that means to have many forms or faces
#Poly = many ,   Morphe = form
#  INHERITANCE = AN OBJECT COULD BE TREATED OF THE OF THE SAME TYPE AS A PARENT class
from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2

class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height *0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


shapes = [Circle(4), Square(5), triangle(6,7), Pizza("Pepperoni", 20)]

for shape in shapes:
    print(shape.area(), "cm^2")

