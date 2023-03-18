# Estudiante: Bascope Castro Juan Victor
# Carrera: Ing. de Sistemas.
import sys
import time
from nodos.Nodos import Nodo

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
                hijo = nodo_actual.get_estado().copy() # [:] para guardar una copia
                auxi = hijo[i]
                hijo[i] = hijo[i+1]
                hijo[i+1] = auxi
                hijo_1 = Nodo(hijo) # tomamos el nodo en su modelo
                if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_1)
                mis_hijos.append(hijo_1) # agregamos en el array los nodos
                i = i + 1
                  
            nodo_actual.set_hijo(mis_hijos)

# metodo para validar que los valores sean correctos entre ambos arreglo
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
    if(valores >= len(arr1)): return True
    else: return False




if __name__ == "__main__":
    estado_inicial = [7, 6, 5, 4, 3, 2, 1, 0]
    solucion = [0, 1, 2, 3, 4, 5, 6, 7]

    # estado_inicial = []
    # solucion = []
    # ingrear la longitud de la secuencia
    # n = int(input('Ingresar la longitud del arreglo: '))
    # for i in range(0, n):
    #     x = input(f'Ingresar en valor de estado inicial en la posicion {i}: ')
    #     estado_inicial.append(x)
    # # ingresamos los valores de la solucion
    # for i in range(0, n):
    #     x = input(f'Ingresar en valor de la solucion en la posicion {i}: ')
    #     solucion.append(x)
    # # verificamos si los valores coiciden entre los dos arreglo
    # todo_correcto = verificarArray(estado_inicial, solucion)
    # if(todo_correcto == False): 
    #     sys.exit('Los valores entre ambos arreglos no coinciden!')
    
    
    tiempo_inicial = time.time()
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
    print("Nodos abiertos: ", len(resultado))
    tiempo_trascurrido = round(time.time()-tiempo_inicial, 10)
    print('Duracion:', (tiempo_trascurrido % 60) , 'segundos')

