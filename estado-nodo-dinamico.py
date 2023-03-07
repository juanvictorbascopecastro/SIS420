import sys

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = None
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        self.hijo = hijo
        if self.hijo is not None:
            for s in self.hijo:
                s.padre = self

    def get_hijo(self):
        return self.hijo
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre
    
    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, Nodo):
        if self.get_estado() == Nodo.get_estado():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_estado())


def cambiar_estado(nodo, i, j):
    nodo[j], nodo[i] = nodo[i], nodo[j] # el nodo en la posicion j debe tomar el siguiente valor
    return nodo


def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # operador dinamico (Accion uno, intercambiar la posicion 0 con la 1 del estado)
            mis_hijos = [] # declaramos un array para guardar los nodos
            i = 0
            while (i < len(nodo_actual.get_estado())-1):
                # expandir nodos hijo
                hijo = nodo_actual.get_estado().copy()
                auxi = hijo[i]
                hijo[i] = hijo[i+1]
                hijo[i+1] = auxi
                hijo_1 = Nodo(hijo) # tomamos el nodo en su modelo
                if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_1)
                mis_hijos.append(hijo_1) # agregamos en el array los nodos
                i = i + 1
                  
            nodo_actual.set_hijo(mis_hijos)

def verificarArray(arr1, arr2):
    cont = 0
    valores = 0
    while(cont < len(arr1)):
        cont2 = 0
        while(cont2 < len(arr2)):
            if(arr1[cont] == arr2[cont2]):
                valores +=1
                cont2 = len(arr2) # para salir del bucle
            cont2 += 1
        cont += 1
    print(valores, len(arr2))
    if(valores >= len(arr1)): return True
    else: return False




if __name__ == "__main__":
    # estado_inicial = [3, 2, 0, 1, 4]
    # solucion = [0, 1, 2, 3, 4]
    estado_inicial = []
    solucion = []
    
    # ingrear la longitud de la secuencia
    n = int(input('Ingresar la longitud del arreglo: '))
    for i in range(0, n):
        x = input(f'Ingresar en valor de estado inicial en la posicion {i}: ')
        estado_inicial.append(x)
    # ingresamos los valores de la solucion
    for i in range(0, n):
        x = input(f'Ingresar en valor de la solucion en la posicion {i}: ')
        solucion.append(x)
    # verificamos si los valores coiciden entre los dos arreglo
    todo_correcto = verificarArray(estado_inicial, solucion)
    if(todo_correcto == False): 
        sys.exit('Los valores entre ambos arreglos no coinciden!')
    
    # SI TODO ESTA CORRECTO CONTINUAMOS CON LA SOLUCION
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    # print(nodo_actual)
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)