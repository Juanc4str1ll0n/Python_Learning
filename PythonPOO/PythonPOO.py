class Estudiante:
    
    sexo = "Masculino"                               #Variables de la clase, se definen afuera del constructor y son globales
    prom = 2022
    num_estudiantes = 0

    def __init__(self, nombre, edad, documento):     #Variables de constructor --> se definen en el constructor
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        Estudiante.num_estudiantes += 1

    def calcular_promedio(self, *args):
        sum = 0
        for i in args:
            sum += i
        prom = sum / len(args)
        print("El promedio es: " , prom)



Estudiante1 = Estudiante("Juan", 19, 1116240244)

Estudiante1.calcular_promedio(1,2,3,4,5,5)
print(Estudiante1.prom)

print(Estudiante.num_estudiantes)

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

#multiple inheritance = inherit from more than one parent class
#                       C(A,B)

class Prey:                                 #clase presa
    def flee(self):
        print("This animal is fleeing")   #Huir, 

class Predator:     
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()


rabbit.flee()