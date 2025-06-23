#class methods --> Allow operations related to the class itself
#                   take cls as the first parameter, which represents the class itself

# Es un método que no trabaja con una instancia individual, sino con la clase en general. 
# En lugar de recibir self (que representa un objeto individual), recibe cls, que representa la clase entera.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return Student.total_gpa / Student.count


student1 = Student("Juan", 3.5 )
student2 = Student("Valery", 4 )
student3 = Student("David", 4.2 )

print(Student.get_count())  
print(Student.get_average_gpa()) 