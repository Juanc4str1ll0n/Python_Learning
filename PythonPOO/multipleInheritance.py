#multiple inheritance = inherit from more than one parent class
#                       C(A,B)

#En este caso las clases predador y presa osn heredadas dependiendo
#Por otro lado un depredador y presa heredan de una clase animal a la vez

class Animal:
     
    def __init__(self, name):
        self.name = name 

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eatimg ")



class Prey(Animal):                                 #clase presa
    def flee(self):
        print(f"{self.name} is fleeing")   #Huir, 

class Predator(Animal):
    def hunt(self):    
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Leo")
fish = Fish("Larry")


rabbit.flee()
fish.hunt()
hawk.eat()

