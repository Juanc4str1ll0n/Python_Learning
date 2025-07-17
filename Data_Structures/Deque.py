# Diferencia entre Queue y Deque:
# - Queue (Cola): estructura de datos FIFO (First-In, First-Out).
#   Solo permite insertar elementos por el final (enqueue) y eliminarlos por el frente (dequeue).
#   Ejemplo típico: fila del supermercado.

# - Deque (Double Ended Queue o Cola Doble): estructura más flexible que permite inserciones
#   y eliminaciones tanto por el frente como por el final.
#   Soporta operaciones como: insertar al inicio (offerFirst), insertar al final (offerLast),
#   eliminar del inicio (pollFirst) y eliminar del final (pollLast).
#   Es útil para casos donde se necesita tanto comportamiento FIFO como LIFO.

class Node:
    def __init__(self, dato):
        self.data = dato
        self.siguiente = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.cabeza = None
        self.final = None