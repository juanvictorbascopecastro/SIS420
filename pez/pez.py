'''Aplicar el algoritmo de busqueda profundidad (version recursiva) para resolver el probleme del juego de palitos  de fosforo, 
donde se debe mover dos palitos para cambiar de direccion al pez.'''
from Nodo import Nodo

class Pez:  
    def __init__(self, data = None):
        self.data = data
            
    # metodo para cambiar el valor
    def cambiarValor(self, nodo):
        for i in range(0, len(nodo.get_estado())-1):
            hijo = nodo.get_estado().copy()
            auxi = hijo[i]
            hijo[i] = hijo[i+1]
            hijo[i+1] = auxi
            modelo = Nodo(hijo)
            nodo.set_hijo(modelo)
        return nodo
        
    def heuristica(self, nodo, solucion):
        list = []
        nodo = nodo.get_estado()
        for i in range(1, len(nodo)): # recorremos todas las alternativas empezando en la posicion 1
            if(nodo[i] == solucion[i]): list.append(1)
            else: list.append(0)

        return sum(list)
        
    def printPezInicial(pez):
        print('Pez Inicial')
        str = ''
        for i in range(0, len(pez)):
            if(i != 0 and i % 3 == 0): 
                print(str)
                str = ''
            str = str + pez[i]
        print(str)

    def printPezFinal(pez):
        print('Pez Final')
        str = ''
        for i in range(len(pez)):
            str = str + pez[i]
            if(i == 3 or i == 7): 
                print(str)
                str = ''
        print(str)
    
    # este metodo recorre el vector verificando cada posicion
    def dfs(self, nodo_inicial, nodo_solucion, visitado):
        visitado.append(nodo_inicial.get_estado())
        if nodo_inicial.get_estado() == nodo_solucion:
            return nodo_inicial
        else:
            nodo_inicial = self.cambiarValor(nodo_inicial)

            for nodo_hijo in nodo_inicial.get_hijo():
                res = self.heuristica(nodo_inicial, nodo_solucion)
                # si el nodo hijo no esta en visitados
                if not nodo_hijo.get_estado() in visitado and res >= 5: # en la heolistica verificamos cuantos deben estar en su posicion para entrar a todos sus nodos hijos
                    # volvemos a llamar al metodo recursivamente
                    Solution = self.dfs(nodo_hijo, nodo_solucion, visitado)
                    if Solution is not None:
                        return Solution
            return None

if __name__ == "__main__":    
    estado_inicial = [
        ' ', '\\', ' ',
        '\\', '/', '\\',
        '/', '\\', '/',
        ' ', '/', ' '
    ]
    Pez.printPezInicial(estado_inicial)
    estado_objetivo = [
        ' ', '/', '\\', ' ',
        '/', '\\', '/', '\\',
        ' ', '/', '\\', ' '
    ]
    nodo_inicial = Nodo(estado_inicial)
    nodo_actual = Pez().dfs(nodo_inicial, estado_objetivo, [])

    # Mostrar Resultado
    resultado = []
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    Pez.printPezFinal(resultado[len(resultado)-1])

