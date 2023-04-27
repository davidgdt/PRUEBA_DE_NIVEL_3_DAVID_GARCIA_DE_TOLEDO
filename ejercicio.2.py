class Heap:
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

    def agregar(self, dato):
        self.vector[self.tamanio] = dato
        self.flotar(self.tamanio)
        self.tamanio += 1

    def quitar(self):
        self.intercambio(0, self.tamanio - 1)
        dato = self.vector[self.tamanio - 1]
        self.tamanio -= 1
        self.hundir(0)
        return dato

    def heap_vacio(self):
        return self.tamanio == 0

    def flotar(self, indice):
        while indice > 0 and self.vector[indice][0] > self.vector[(indice - 1) // 2][0]:
            padre = (indice - 1) // 2
            self.intercambio(indice, padre)
            indice = padre

    def hundir(self, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while control and hijo_izq < self.tamanio:
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if hijo_der < self.tamanio:
                if self.vector[hijo_der][0] > self.vector[hijo_izq][0]:
                    aux = hijo_der
            if self.vector[indice][0] < self.vector[aux][0]:
                self.intercambio(indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False

    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()[1]

    def intercambio(self, indice1, indice2):
        self.vector[indice1], self.vector[indice2] = self.vector[indice2], self.vector[indice1]


class nodoPila:
    # Corrección: indentación en las siguientes dos líneas
    info = None
    sig = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima
        self.cima = nodo
        self.tamanio += 1

    def desapilar(self):
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1
        return x

    def pila_vacia(self):
        return self.cima is None

def prioridad(pedido):
    nombre, multiverso, descripcion = pedido
    if (nombre == "Gran Conquistador" or multiverso == "616" or "El que permanece" in descripcion):
        return 1
    elif (nombre == "Khan que todo lo sabe" or "Carnicero de Dioses" in descripcion or multiverso == "838"):
        return 2
    else:
        return 3

