#PERTENECE A LA CLASE NO A NINGUN OBJETO CREADO DE LA CLASE

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("SpongeBob", "Cook")

print(Employee.is_valid_position("Doctor"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


#Ejemplo 2 

class Calculadora:
    @staticmethod
    def sumar(*args):
        sum = 0
        for i in args:
            sum+= i
        print(sum)

    @staticmethod
    def multiplicar(*args):
        mult = 1
        for i in args:
            mult = mult*i
        print(mult)

Calculadora.sumar(1,2,3)
Calculadora.multiplicar(5,4)

