class Nodo :
    def __init__ (self, valor):
        self.valor = valor
        self.siguiente = None

class Cola :
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.isEmpty():  # Si la cola está vacía
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo  # Agregar el nuevo nodo al final
            self.final = nuevo_nodo            # Actualizar el final de la cola
        self.tamano += 1  # Incrementar el tamaño de la cola

   