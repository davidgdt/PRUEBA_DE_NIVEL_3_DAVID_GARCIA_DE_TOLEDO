import random

class Nodo:
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def pila_vacia(self):
        return len(self.items) == 0

class Cola:
    def __init__(self):
        self.items = []

    def arribo(self, item):
        self.items.append(item)

    def atencion(self):
        return self.items.pop(0)

    def cola_vacia(self):
        return len(self.items) == 0

def insertar_nodo(raiz, info):
    if raiz is None:
        raiz = Nodo(info)
    elif info < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, info)
    else:
        raiz.der = insertar_nodo(raiz.der, info)
    return raiz

def cargar_numeros_aleatorios(n):
    arbol = None
    for _ in range(n):
        arbol = insertar_nodo(arbol, random.randint(1, 1000))
    return arbol

def preorden_iterativo(raiz):
    if raiz is None:
        return
    pila = Pila()
    pila.apilar(raiz)

    while not pila.pila_vacia():
        nodo = pila.desapilar()
        print(nodo.info)

        if nodo.der is not None:
            pila.apilar(nodo.der)
        if nodo.izq is not None:
            pila.apilar(nodo.izq)

def inorden_iterativo(raiz):
    pila = Pila()
    nodo_actual = raiz

    while not pila.pila_vacia() or nodo_actual is not None:
        if nodo_actual is not None:
            pila.apilar(nodo_actual)
            nodo_actual = nodo_actual.izq
        else:
            nodo_actual = pila.desapilar()
            print(nodo_actual.info)
            nodo_actual = nodo_actual.der

def postorden_iterativo(raiz):
    pila1 = Pila()
    pila2 = Pila()
    pila1.apilar(raiz)

    while not pila1.pila_vacia():
        nodo = pila1.desapilar()
        pila2.apilar(nodo)

        if nodo.izq is not None:
            pila1.apilar(nodo.izq)
        if nodo.der is not None:
            pila1.apilar(nodo.der)

    while not pila2.pila_vacia():
        nodo = pila2.desapilar()
        print(nodo.info)

def contar_pares_impares_iterativo(raiz):
    pares = 0
    impares = 0
    cola = Cola()
    cola.arribo(raiz)

    while not cola.cola_vacia():
        nodo = cola.atencion()

        if nodo.info % 2 == 0:
            pares += 1
        else:
            impares += 1

        if nodo.izq is not None:
            cola.arribo(nodo.izq)
    






