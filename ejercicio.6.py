import random

class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nodo = NodoPila(dato)
        nodo.siguiente = self.tope
        self.tope = nodo

    def desapilar(self):
        if self.tope is not None:
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            return dato
        else:
            return None

    def esta_vacia(self):
        return self.tope is None

    def ver_tope(self):
        if self.tope is not None:
            return self.tope.dato
        else:
            return None

def generar_mazo():
    palos = ["espada", "basto", "copa", "oro"]
    mazo = Pila()

    cartas = [(palo, numero) for palo in palos for numero in range(1, 13)]
    random.shuffle(cartas)

    for carta in cartas:
        mazo.apilar(carta)

    return mazo

def separar_por_palo(mazo):
    pilas_por_palo = {"espada": Pila(), "basto": Pila(), "copa": Pila(), "oro": Pila()}

    while not mazo.esta_vacia():
        carta = mazo.desapilar()
        pilas_por_palo[carta[0]].apilar(carta)

    return pilas_por_palo

def ordenar_pila(pila):
    pila_ordenada = Pila()
    lista_cartas = []

    while not pila.esta_vacia():
        carta = pila.desapilar()
        lista_cartas.append(carta)

    lista_cartas.sort(key=lambda x: x[1])

    for carta in lista_cartas:
        pila_ordenada.apilar(carta)

    return pila_ordenada

def imprimir_pila(pila):
    while not pila.esta_vacia():
        print(pila.desapilar())


# Generar mazo y separar por palo
mazo = generar_mazo()
pilas_por_palo = separar_por_palo(mazo)

# Seleccionar el palo a ordenar (por ejemplo, "espada")
palo_a_ordenar = "espada"
pila_ordenada = ordenar_pila(pilas_por_palo[palo_a_ordenar])

# Imprimir pila ordenada
print(f"Pila de {palo_a_ordenar} ordenada:")
imprimir_pila(pila_ordenada)
