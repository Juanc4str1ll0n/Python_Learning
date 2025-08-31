# class Node:
#     def __init__(self):
#         self.hijos = {}

# dictionary = {}

# dictionary['g'] = Node()
# dictionary['l'] = Node()

# print(dictionary)

#-- TICKETS

import datetime
encendido = True

def recibo(productos:list, precios:list):
    subtotal = 0
    print("|-----------------------------------|",
        "\n|           |RECIBO|                |",
        "\n|-----------------------------------|",
        f"\n|       {dia_actual}      |",
        "\n|-----------------------------------|",
        "\n| Producto                   Precio |")
    for i in range(len(productos)):
        subtotal += precios[i]
        print(f"| {productos[i]:20}  ${precios[i]:>11}|")
    impuestos = subtotal * 0.19
    print("|-----------------------------------|",
        f"\n|Subtotal:             {subtotal}|",
        f"\n|Impuestos (19%)       {impuestos}|",
        f"\n|Total:                {(subtotal + impuestos)}|",
        f"\n|----------------------------------|"
        f"\n|Gracias por tu compra             |") 

productos = []
precios = []
dia_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
while encendido:
    try:
        prod = input("Ingrese el nombre de un producto:  ")
        if not prod:
            print("Error, Ingresa un producto")
            continue
        
        precio = int(input("Ingrese el precio del producto:  "))
        productos.append(prod)
        precios.append(precio)
        
        opcion = input("Quieres agregar mas productos? (S/N):  ")
        
        if opcion == "N":
            encendido = False
            recibo(productos, precios)
    except ValueError: 
        print("Error, por favor ingresar un valor valido")
        pass   