"""A partir del codigo de rompecabezas lineal, para n digitos, 
aplicar una heuristica y resolver el mismo, identificando, 
cual es la capacidad maxima de resolucion y el tiempo que aplica para dicho proposito. Debe probar al menos 3 heuristicas diferentes, 
pueden ser las recomendadas en clase u otra considere adecuada y demostrar cual el la mejor de las tres."""
# LA ALTERNATIVA 1 DE FORMA RECURSIVA
# EN ESTA ALTERNATIVA LA LONGITUD MAXIMA QUE SOPORTA ES 44
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) # Con la libreria Path debemos obtener la ruta base para importar nuestros metodos

from Metodos import Metodos # importamos el metodo para validar array
from NodosBI import NodoBI 

def busqueda_heuristica(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        mis_hijos = [] # declaramos un array para guardar los nodos
        i = 0
        while (i < len(nodo_inicial.get_estado())-1):
            # expandir nodos hijo
            hijo = nodo_inicial.get_estado().copy() # [:] para guardar una copia
            auxi = hijo[i]
            hijo[i] = hijo[i+1]
            hijo[i+1] = auxi
            hijo_1 = NodoBI(hijo) # tomamos el nodo en su modelo
            mis_hijos.append(hijo_1) # agregamos en el array los nodos
            i = i + 1
        nodo_inicial.set_hijo(mis_hijos)

        for hijo_node in nodo_inicial.get_hijo():
            if not hijo_node.get_estado() in visitados and heuristica(nodo_inicial, hijo_node): # si no esta en visitados y acepta la condicion de la euristica
            #if not hijo_node.get_estado() in visitados:
                # Llamada recursiva
                solu = busqueda_heuristica(hijo_node, solucion, visitados)
                if solu is not None:
                    return solu
                
        return None

# esta alternativa si la posicion es mayor que el anterior suma, en el nodo hijo y el padre, y los resultado debe ser el hijo mayor que el padre
def heuristica(padre_node, hijo_node):
    padre_quality = 0
    hijo_quality = 0
    padre_data = padre_node.get_estado()
    hijo_data = hijo_node.get_estado()

    for n in range(1, len(padre_data)): # recorremos todas las alternativas empezando en la posicion 1
        if padre_data[n] > padre_data[n - 1]:
            padre_quality = padre_quality + 1 
        if hijo_data[n] > hijo_data[n - 1]:
            hijo_quality = hijo_quality + 1

    if hijo_quality >= padre_quality:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        estado_inicial = []
        estado_solucion = []

        # generamos los valores de los estados inicial y final limite 44
        contador = 8
        for n in list(range(9)):
            estado_inicial.append(contador+1)
            estado_solucion.append(n+1)
            contador -= 1

        print("Estado Inicial: ", estado_inicial)
        print("Estado Solucion: ", estado_solucion)

        todo_correcto = Metodos.logitudIguales(estado_inicial, estado_solucion)
        if(todo_correcto == False): 
            sys.exit('Los valores entre ambos arreglos no coinciden!')

        visitados_nodes = []
        inicio_time = time.time()
        nodo_inicial = NodoBI(estado_inicial)
        nodo_solucion = busqueda_heuristica(nodo_inicial, estado_solucion, visitados_nodes)

        resultado = []
    
        node = nodo_solucion
        while node.get_padre() is not None:
            resultado.append(node.get_estado())
            node = node.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        fin_time = time.time()
       
        print(resultado)
        print("Nodos abiertos: ", len(resultado))
        print("Tiempo de ejecucion: ", fin_time - inicio_time)
    except RuntimeError as err:
       print("ESTA ALTERNATIVA TIENE UN SOPORTE PARA ARREGLOS CON LOGITUD MAXIMA 44")