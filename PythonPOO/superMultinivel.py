#Ejemplo de herencia multinivel con super
class A:
    def __init__(self):
        print("Inicializando clase A")

    def saludar(self):
        print("Hola desde A")

class B(A):
    def __init__(self):
        print("Inicializando clase B")
        super().__init__()  # Llama al constructor de A

    def saludar(self):
        print("Hola desde B")
        super().saludar()  # Llama a saludar() de A

class C(B):
    def __init__(self):
        print("Inicializando clase C")
        super().__init__()  # Llama al constructor de B (que a su vez llama a A)

    def saludar(self):
        print("Hola desde C")
        super().saludar()  # Llama a saludar() de B (que a su vez llama a A)

# Crear objeto de clase C
obj = C()
obj.saludar()
