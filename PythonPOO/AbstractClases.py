#En las clases abstractas el usuario no puede crear un objeto de esa clase
#Para ello importamos abc -> abstract base clase
# e importamos ABC Y ABSTRACTMETHOD 

from abc import ABC, abstractmethod


#En etse ejemplo se crea una lcase abstracta vehiculo con un constructor, este es para las clases que sean heredadas
#de esta manera no se crea un vehiculo como tal porque seria muy especifico, sino objetos de clases que la heredan
#como un auto o una moto


class Vehiculo(ABC):
    def __init__(self, marca, modelo, combustible_actual):
        self.marca = marca
        self.modelo = modelo
        self.combustible_actual = combustible_actual
        self.en_marcha = False

    def arrancar(self):
        self.en_marcha = True
        print(f"{self.marca} {self.modelo} ha arrancado")

    def detener(self):
        self.en_marcha = False
        print(f"{self.marca} {self.modelo} se ha detenido. ")

    #METODOS ABSTRACTOS
    #ESTOS METODOS DEBEN IMPLEMENTARSE EN TODAS LAS CLASES QUE HEREDEN

    @abstractmethod
    def obtener_tipo(self):
        pass   

    @abstractmethod
    def calcular_autonomia(self):
        pass

    @abstractmethod
    def necesita_mantenimiento(self):
        pass


#Subclase Auto que implementa todos los metodos
class Auto(Vehiculo):
    def __init__(self, marca, modelo, combustible_actual, km_por_litro, km_recorridos):
        super().__init__(marca, modelo, combustible_actual)
        self.km_por_litro = km_por_litro
        self.km_recorridos = km_recorridos

    def obtener_tipo(self):
        return "Auto"

    def calcular_autonomia(self):
        return self.combustible_actual * self.km_por_litro

    def necesita_mantenimiento(self):
        return self.km_recorridos >= 10000

#Subclase moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, combustible_actual, eficiencia):
        super().__init__(marca, modelo, combustible_actual)
        self.eficiencia = eficiencia  # km/litro
        self.revisiones = 2  # cantidad de revisiones hechas

    def obtener_tipo(self):
        return "Moto"

    def calcular_autonomia(self):
        return self.combustible_actual * self.eficiencia

    def necesita_mantenimiento(self):
        return self.revisiones < 1



