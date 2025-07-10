#En este caso le puedo indicar en una funcion el tipo de dato que se becesita recibir
#De esta manera estamos documentando la funcion, la flecha sirve para decir que va a retornar
#Cierto tipo de valor

def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

def sumar(num1: int, num2:int) -> int:
    return num1 + num2