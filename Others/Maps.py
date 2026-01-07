# Aplica una función a cada elemento de una lista (o cualquier iterable) 
# y devuelve un objeto map (que puedes convertir en lista).

# Sintaxis:

# map(funcion, iterable)

def dividir_en_dos(num):
    return num / 2

my_list = [5, 2, 10, 20, 54, 27, 30]
my_list2 = map(dividir_en_dos, my_list)


print(list(my_list2))


def funcion(algo):
    print("Hola")

my_list2 = map(funcion, my_list)
print(list(my_list2))
