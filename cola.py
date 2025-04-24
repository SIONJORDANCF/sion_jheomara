class Nodo :
    def __init__ (self, valor):
        self.valor = valor
        self.siguiente = None

class Cola :
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0

    def enqueue(self, valor): #este lo llame cola no por su nombre cuando hice el commit
        nuevo_nodo = Nodo(valor)
        if self.isEmpty():  # Si la cola está vacía
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo  # Agregar el nuevo nodo al final
            self.final = nuevo_nodo            # Actualizar el final de la cola
        self.tamano += 1  # Incrementar el tamaño de la cola

    def desencolar(self):
        if self.is_empty():
            raise IndexError("No se puede desencolar de una cola vacía")
        dato = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamanho -= 1
        return dato
    
    def is_empty(self):
        return self.frente is None
    
    def peek(self):
        if self.is_empty():
            raise IndexError("No se puede ver el frente de una cola vacía")
        return self.frente.valor 
    
    #jheomara solo harias la size que el tamanho esa funcion nomaj te falta y ya estaria todo y si lo haces el metodo mostrar mas para poder
    #mostra lo q se ejecuta vale solo implementas la funcion mostrar y ya estaria esos dos nomaj 