class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamano = 0

    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.is_empty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar(self):
        if self.is_empty():
            raise IndexError("No se puede desencolar de una cola vacía")
        dato = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamano -= 1
        return dato

    def is_empty(self):
        return self.frente is None

    def peek(self):
        if self.is_empty():
            raise IndexError("No se puede ver el frente de una cola vacía")
        return self.frente.valor

    def size(self):
        return self.tamano

# Prueba
cola = Cola()
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Frente:", cola.peek())         # 10
print("Tamaño:", cola.size())         # 3
print("Desencolar:", cola.desencolar())  # 10
print("Frente nuevo:", cola.peek())   # 20
print("¿Está vacía?", cola.is_empty()) # False