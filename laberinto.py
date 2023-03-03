# Victor Bascope 
# Ing. de Sistemas
laberinto = [
    [0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0]
]
# print(posiciones)
def recorrer_laberinto():
    fila = 0
    columna = 0
    movimientos = ['abajo']
    n = len(laberinto) # logintud de la matris 8 * 8
    while(fila < n-1 and columna < n-1):
        ultimo = len(movimientos)-1
        if(movimientos[ultimo] != 'arriba' and fila + 1 < n and laberinto[fila+1][columna] != 1):
            fila += 1
            movimientos.append('abajo')
        elif(movimientos[ultimo] != 'abajo' and fila - 1 > 0 and laberinto[fila-1][columna] != 1):
            fila -=1
            movimientos.append('arriba')
        elif(movimientos[ultimo] != 'izquierda' and columna + 1 < n and laberinto[fila][columna+1] != 1):
            columna += 1
            movimientos.append('derecha')
        elif(movimientos[ultimo] != 'derecha' and columna - 1 > 0 and laberinto[fila][columna-1] != 1):
            columna -= 1
            movimientos.append('izquierda')
        else: 
            movimientos.append('no hay salida')
    return movimientos

print(recorrer_laberinto())