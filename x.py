class Person:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def beber(self, bebida):
        print(f"Estoy bebiendo {bebida}")

    def comer(self, comida):
        print(F"Estoy comiendo {comida}")

    def __str__(self):
        return F"La persona se llama {self.nombre}, la edad es {self.edad}, la profesion es {self.profesion}"

    def __add__(self, other):
        return self.edad + other.edad

Juan = Person("Juan", 18, "Ingeniero")
Edgar = Person("Edgar", 19, "Medico")


print(Juan)
print(Juan + Edgar)