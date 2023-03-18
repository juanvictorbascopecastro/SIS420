# LA ALTERNATIVA 2 BUSQUEDA EN PROFUNDIDAD
# EN ESTA ALTERNATIVA LA LOGITUD MAXIMA QUE SOPORTA ES 44
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) # Con la libreria Path debemos obtener la ruta base para importar nuestros metodos

from Metodos import Metodos # importamos el metodo para validar array
from password.Nodos import Nodo 

def busqueda_BPPR(nodo_inicial, solucion, visitado, auxi_numero):
    #nodo_inicial = random.sample(range(0,5),5)
    visitado.append(nodo_inicial.get_estado())
    if nodo_inicial.get_estado() == solucion:
        return nodo_inicial
    else:
        #Bucle para recorrer 
        for i in range(0, len(solucion)-1):
            indice = i
                
            hijo_datos = nodo_inicial.get_estado().copy()
            temp = hijo_datos[indice]
            hijo_datos[indice] = hijo_datos[indice + 1]
            hijo_datos[indice + 1] = temp
            hijo = Nodo(hijo_datos)
            nodo_inicial.set_hijo(hijo)
        
        for nodo_hijo in nodo_inicial.get_hijo():
            numero_validador = heuristica(nodo_hijo, solucion)
            if not nodo_hijo.get_estado() in visitado and numero_validador <= auxi_numero:
                # Llamada Recursiva
                Solution = busqueda_BPPR(nodo_hijo, solucion, visitado, numero_validador)
                if Solution is not None:
                    return Solution
        return None
    
# se pasa un padre y la solucion
def heuristica(hijo_node, solucion):
    hijo_data = hijo_node.get_estado()
    list = [];
    for n in range(0, len(hijo_data)): # revisa todos los valores del padre
        # el nodo actual se resta sus posiciones y se convierte en valor absoluto para obtener que tan lejos esta de lo que deberia estar
        # EJEMPLO solucion = 1, 2, 3, 4  nodo_actual = 4, 3, 2, 1 entonces son 4 iteraciones 1-4=3, 2-3=1, 3-2=1, 4-1=3
        list.append(abs(hijo_data[n] - solucion[n])) # agregamos a una lista los valores 

    return sum(list) # devolvemos la suma que seria 8 
    
if __name__ == "__main__":    
    try:
        # estado_inicial = [3, 2, 1, 0]
        # estado_objetivo = [0, 1, 2, 3]
        estado_inicial = []
        estado_objetivo = []

        contador = 5
        for n in list(range(6)):
            estado_inicial.append(contador+1)
            estado_objetivo.append(n+1)
            contador -= 1

        print("Estado Inicial", estado_inicial)
        print("Solucion", estado_objetivo)
        nodo_solucion = None
        visitado = []
        # estado_inicial = random.sample(range(0,n),n)
        nodo_inicial = Nodo(estado_inicial)
        inicio = time.time()
        nodo_actual = busqueda_BPPR(nodo_inicial, estado_objetivo, visitado, sum(estado_inicial))
        fin = time.time()

        # Mostrar Resultado
        resultado = []
        while nodo_actual.get_padre() is not None:
            resultado.append(nodo_actual.get_estado())
            nodo_actual = nodo_actual.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
        print("Nodos abiertos: ", len(resultado))
        print("Tiempo de ejecucion: ", fin - inicio)
    except RuntimeError as err:
       print("ESTA ALTERNATIVA TIENE UN SOPORTE PARA ARREGLOS CON LOGITUD MAXIMA 8")