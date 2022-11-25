from collections import deque

class EstadoPuzzle:
    def __init__(self, estado, padre, movimiento, profundidad, costo, llave):
        self.estado = estado
        self.padre = padre
        self.movimiento = movimiento
        self.profundidad = profundidad
        self.costo = costo
        self.llave = llave
        if self.estado:
            self.mapa = ''.join(str(e) for e in self.estado)
            def __eq__(self,other):
                return self.mapa == other.mapa
            def __lt__(self, other):
                return self.mapa < other.mapa
            def __str__(self):
                return str(self.mapa)

EstadoObjetivo = [1,2,3,4,5,6,7,8,0]
NodoObjetivo = None
NodosExpandidos = 0
BusquedaProfundidad = 0
AlturaMaxima = 5

def dfs(estadoIncial):
    global NodoObjetivo, BusquedaProfundidad, AlturaMaxima

    caminoVisitado = set()
    pila = list([EstadoPuzzle(estadoIncial, None, None, 0, 0, 0)])
    while pila:
        nodo = pila.pop()
        caminoVisitado.add(nodo.mapa)
        if nodo.estado == EstadoObjetivo:
            NodoObjetivo = nodo
            return pila
        caminosPosibles = reversed(subNodos(nodo))
        for camino in caminosPosibles:
            if camino.mapa not in caminoVisitado:
                if camino.profundidad < AlturaMaxima:
                    pila.append(camino)
                caminoVisitado.add(camino.mapa)
                if camino.profundidad > BusquedaProfundidad:
                    BusquedaProfundidad = 1 + BusquedaProfundidad

def subNodos(nodo):
    global NodosExpandidos
    NodosExpandidos = NodosExpandidos + 1

    siguienteCaminos = []
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 1), nodo, 1, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 2), nodo, 2, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 3), nodo, 3, nodo.profundidad + 1, nodo.costo + 1, 0))
    siguienteCaminos.append(EstadoPuzzle(Movimiento(nodo.estado, 4), nodo, 4, nodo.profundidad + 1, nodo.costo + 1, 0))
    nodos = []
    for camino in siguienteCaminos:
        if(camino.estado != None):
            nodos.append(camino)
    return nodos

def Movimiento(estado, direccion):
    nuevoEstado = estado[:]

    indice = nuevoEstado.index(0)

    if indice == 0:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[0]
            nuevoEstado[0] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[0]
            nuevoEstado[0] = nuevoEstado[1]
            nuevoEstado[1] = temp
        return nuevoEstado
    elif indice == 1:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 3:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[0]
            nuevoEstado[0] = temp
        elif direccion == 4:
            temp = nuevoEstado[1]
            nuevoEstado[1] = nuevoEstado[2]
            nuevoEstado[2] = temp
        return nuevoEstado
    elif indice == 2:
        if direccion == 1:
            return None
        elif direccion == 2:
            temp = nuevoEstado[2]
            nuevoEstado[2] = nuevoEstado[5]
            nuevoEstado[5] = temp
        elif direccion == 3:
            temp = nuevoEstado[2]
            nuevoEstado[2] = nuevoEstado[1]
            nuevoEstado[1] = temp
        elif direccion == 4:
            return None
        return nuevoEstado
    elif indice == 3:
        if direccion == 1:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[0]
            nuevoEstado[0] = temp
        elif direccion == 2:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[6]
            nuevoEstado[6] = temp
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[3]
            nuevoEstado[3] = nuevoEstado[4]
            nuevoEstado[4] = temp
        return nuevoEstado
    elif indice == 4:
        if direccion == 1:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[1]
            nuevoEstado[1] = temp
        elif direccion == 2:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[7]
            nuevoEstado[7] = temp
        elif direccion == 3:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 4:
            temp = nuevoEstado[4]
            nuevoEstado[4] = nuevoEstado[5]
            nuevoEstado[5] = temp
        return nuevoEstado
    elif indice == 5:
        if direccion == 1:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[2]
            nuevoEstado[2] = temp
        elif direccion == 2:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[8]
            nuevoEstado[8] = temp
        elif direccion == 3:
            temp = nuevoEstado[5]
            nuevoEstado[5] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 4:
            return None
        return nuevoEstado
    elif indice == 6:
        if direccion == 1:
            temp = nuevoEstado[6]
            nuevoEstado[6] = nuevoEstado[3]
            nuevoEstado[3] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            return None
        elif direccion == 4:
            temp = nuevoEstado[6]
            nuevoEstado[6] = nuevoEstado[7]
            nuevoEstado[7] = temp
        return nuevoEstado
    elif indice == 7:
        if direccion == 1:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[4]
            nuevoEstado[4] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[6]
            nuevoEstado[6] = temp
        elif direccion == 4:
            temp = nuevoEstado[7]
            nuevoEstado[7] = nuevoEstado[8]
            nuevoEstado[8] = temp
        return nuevoEstado
    elif indice == 8:
        if direccion == 1:
            temp = nuevoEstado[8]
            nuevoEstado[8] = nuevoEstado[5]
            nuevoEstado[5] = temp
        elif direccion == 2:
            return None
        elif direccion == 3:
            temp = nuevoEstado[8]
            nuevoEstado[8] = nuevoEstado[7]
            nuevoEstado[7] = temp
        elif direccion == 4:
            return None
        return nuevoEstado

def main():
    global NodoObjetivo, AlturaMaxima
    estadoInicial = [1,2,3,5,6,8,4,7,0]
    while NodoObjetivo == None and AlturaMaxima < 66126:
        #print("Busqueda en profundidad ", AlturaMaxima)
        dfs(estadoInicial)
        if NodoObjetivo == None:
            AlturaMaxima = AlturaMaxima + 50

    movimientos = []
    imprimir = []
    profundidad = BusquedaProfundidad
    if NodoObjetivo != None:
        profundidad = NodoObjetivo.profundidad
        while estadoInicial != NodoObjetivo.estado:
            if NodoObjetivo.movimiento == 1:
                camino = 'Arriba'
            elif NodoObjetivo.movimiento == 2:
                camino = 'Abajo'
            elif NodoObjetivo.movimiento == 3:
                camino = 'Izquierda'
            elif NodoObjetivo.movimiento == 4:
                camino = 'Derecha'
            movimientos.insert(0, camino)
            imprimir.insert(0, NodoObjetivo.estado)
            #print(NodoObjetivo.estado)
            NodoObjetivo = NodoObjetivo.padre

    print("\nResultados Búsqueda Iterativa: \n")
    
    for estado in imprimir:
        print("\t|", estado[0], estado[1], estado[2], "|")
        print("\t|", estado[3], estado[4], estado[5], "|")
        print("\t|", estado[6], estado[7], estado[8], "|")
        print("\n")

    print("Camino: ", movimientos[1:])
    print("Costo: ", len(movimientos))
    print("Nodos expandidos: ",str(NodosExpandidos))
    print("Profundidad: ",str(profundidad))
    print("BusquedaProfundidad: ",str(BusquedaProfundidad))
    print("Altura Maxima: ", AlturaMaxima)

if __name__ == '__main__':
    main()