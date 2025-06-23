#HERENCIA --------------------------------------------------------------

#Clase animal que le va a heredar su constructor y atributos
#a a las demas clases 

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name } is eating ")

    def sleep(self):
        print(f"{self.name } is sleeping ")

class Dog(Animal):
    def speak(self):
        print("guauuu")

class Cat(Animal ):
    def speak(self ):
        print("meow")

class Mouse(Animal ):
    def speak(self):
        print("squeek")


dog = Dog("Mia")
cat = Cat("Larry")
mouse = Mouse("Mickey")

print(dog.isAlive)
dog.eat()
cat.speak()