def buscar_solucion_profundidad(estado_inicial, solucion):
    frontera = [estado_inicial]
    visitados = []
    
    while len(frontera) > 0:
        estado_actual = frontera.pop()
        
        # Verificar si se alcanzó la solución
        if estado_actual == solucion:
            return estado_actual
        
        # Agregar el estado actual a la lista de visitados
        visitados.append(estado_actual)
        
        # Generar los nuevos estados posibles
        nuevos_estados = generar_nuevos_estados(estado_actual)
        
        # Agregar los nuevos estados a la frontera
        for estado in nuevos_estados:
            if estado not in visitados and estado not in frontera:
                frontera.append(estado)
                
    # Si no se encontró solución, retornar None
    return None

def generar_nuevos_estados(estado):
    nuevos_estados = []
    
    # Buscar el índice de los palitos que se pueden mover
    index1 = estado.index('|')
    index2 = estado[index1+1:].index('|') + index1 + 1
    
    # Generar los nuevos estados posibles
    if index2 < len(estado) - 1:
        # Mover los palitos hacia la derecha
        nuevo_estado = list(estado)
        nuevo_estado[index1] = ' '
        nuevo_estado[index2] = ' '
        nuevo_estado[index2+1] = '|'
        nuevo_estado[index2+2] = '|'
        nuevos_estados.append(''.join(nuevo_estado))
        
    if index1 > 1:
        # Mover los palitos hacia la izquierda
        nuevo_estado = list(estado)
        nuevo_estado[index1] = ' '
        nuevo_estado[index1-1] = '|'
        nuevo_estado[index1-2] = '|'
        nuevo_estado[index2] = ' '
        nuevos_estados.append(''.join(nuevo_estado))
        
    return nuevos_estados

# Ejemplo de uso
if __name__ == "__main__":
    estado_inicial = '| | | | |'
    solucion = '| | | | |'

    solucion_encontrada = buscar_solucion_profundidad(estado_inicial, solucion)

    if solucion_encontrada:
        print(f'Solución encontrada: {solucion_encontrada}')
    else:
        print('No se encontró solución')