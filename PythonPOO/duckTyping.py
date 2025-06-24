# Python no verifica el tipo de una variable explícitamente como en Java o C#. 
# En su lugar, verifica si tiene el comportamiento que se espera (métodos, atributos).

# Aunque Person no es una subclase de Duck, como tiene un método quack(), 
# Python lo trata como un “pato”. ¡Eso es duck typing!


class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack like a duck!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)     # Output: Quack!
make_it_quack(person)   # Output: I can quack like a duck!