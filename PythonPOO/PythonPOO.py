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