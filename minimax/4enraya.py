import random
import os
import math

class CuatroEnRaya:
    def __init__(self):
        
        self.tablero = [' ' for i in range(16)]
        if random.randint(0, 1) == 1: # si es 1 X sera el humano
            self.humano = 'X'
            self.coputadora = 'O'
        else: # si no O sera el humano
            self.humano = 'O'
            self.coputadora = 'X'
    # muestra el trablero 
    def ver_trablero(self): 
        print("")
        for i in range(4):
            print(" ", self.tablero[0+(i*3)], ' | ', self.tablero[1+(i*3)], ' | ', self.tablero[2+(i*3)], " | ", self.tablero[3+(i*3)], " ")
            if(i != 3): print("-----------------------")

    def tablero_lleno(self, estado):
        return not ' ' in estado
    
    def hay_ganador(self, estado, jugador):
        if estado[0] == estado[1] == estado[2] == estado[3] == jugador: return True
        if estado[4] == estado[5] == estado[6] == estado[7] == jugador: return True
        if estado[8] == estado[9] == estado[10] == estado[11] == jugador: return True
        if estado[12] == estado[13] == estado[14] == estado[15] == jugador: return True
        
        if estado[0] == estado[4] == estado[8] == estado[12] == jugador: return True
        if estado[1] == estado[5] == estado[9] == estado[13] == jugador: return True
        if estado[2] == estado[6] == estado[10] == estado[14] == jugador: return True
        if estado[3] == estado[7] == estado[11] == estado[15] == jugador: return True

        if estado[0] == estado[5] == estado[10] == estado[11] == jugador: return True
        if estado[12] == estado[9] == estado[6] == estado[3] == jugador: return True
        return False
    
    # verifica si el juego ha finalizado
    def si_el_juego_acabo(self):
        # verificamos si el humano ha ganado
        if self.hay_ganador(self.tablero, self.humano):
            os.system('cls')
            print(f" Gano el humano ({self.humano})!")
            return True
        # verificamos si el computador ha ganado
        if self.hay_ganador(self.tablero, self.coputadora):
            os.system('cls')
            print(f" Gano la computadora ({self.coputadora})!")
            return True
        # ver si no hay mas espacio
        if(self.tablero_lleno(self.tablero)):
            os.system('cls')
            print('El juego finalizo sin ganadores!')
            return True
        
        return False
    
    # 
    def iniciar(self):
        jugador_humano = jugadorHumano(self.humano)
        jugador_computadora = jugadorComputador(self.coputadora)

        while True:
            os.system('cls')
            print(" Turno del", self.humano)
            self.ver_trablero()

            posicion = jugador_humano.mover_humano(self.tablero)
           
            self.tablero[posicion] = self.humano
            print(self.tablero)
            if(self.si_el_juego_acabo()): 
                self.ver_trablero()
                break

            posicion = jugador_computadora.mover_computadora(self.tablero)
            self.tablero[posicion] = self.coputadora
            if(self.si_el_juego_acabo()): 
                self.ver_trablero()
                break


# hace su jugada el humano
class jugadorHumano:
    def __init__(self, letra):
        self.letra = letra
    
    def mover_humano(self, estado):
        while True:
            posicion = int(input("Ingresa tu movida entre [1-16]: "))
            print()
            # en caso de que no volvera a preguntar
            if(posicion > 0 and posicion < 17 and estado[posicion-1] == ' '): # si la casilla esta vacia ponemos su jugada
                break
        return posicion - 1 

# hace su jugada el computador
class jugadorComputador(CuatroEnRaya): #hereda de la clase CuatroEnRaya
    def __init__(self, letra):
        self.letra = letra
        self.humano_letra = 'X' if letra == 'O' else 'O'
    # a quien le toca jugar
    def jugadas(self, estado):
        n = len(estado)
        x = 0
        o = 0
        for i in range(9):
            if(estado[i] == 'X'):
                x = x+1
            if(estado[i] == 'O'):
                o = o+1
        if(self.humano_letra == 'X'):
            return 'X' if x == o else 'O'
        
        if(self.humano_letra == 'O'):
            return 'O' if x == o else 'X'
    # devuelve las posiciones vacias del tablero
    def acciones(self, estado):
        return [i for i, x in enumerate(estado) if x == ' ']
    
    # generamos un tablero nuevo donde ponemos un nuevo movimiento
    def resultado(self, estado, accion):
        nuevo_estado = estado.copy()
        juego = self.jugadas(estado)
        nuevo_estado[accion] = juego
        return nuevo_estado
    
    def ver_ganador(self, estado):
        if(self.hay_ganador(estado, 'X')):
            return True
        if(self.hay_ganador(estado, 'O')):
            return True
        return False
    
    def alfabeta(self, estado, jugador):
        max_jugador = self.humano_letra # el humano busca la maxima posicion
        # la computadora busca la minima posicion
        otro_jugador = 'O' if jugador == 'X' else 'X' 

        if(self.ver_ganador(estado)): # si hubo un tres en raya
            # 1 * (len(self.acciones(estado))+1) if otro_jugador == max_jugador
            if otro_jugador == max_jugador: # si 
                valor = 1 * (len(self.acciones(estado)) + 1) # multiplicamos 1 *  el numero de casillas vacias +1 para evitar ceros
            else:
                valor = -1 * (len(self.acciones(estado)) + 1)

            return {'posicion': None, 'valor': valor} # retornamos un objeto
        elif self.tablero_lleno(estado): # si el tablero esta lleno
            return {'posicion': None, 'valor': 0} 
        
        if(jugador == max_jugador): # si esta jugando el humano
            obj = {'posicion': None, 'valor': -math.inf} 
        else: # si esta jugando la computadora
            obj = {'posicion': None, 'valor': math.inf} 
        
        for posibles_movida in self.acciones(estado): # recorremos los movimientos posible
            # por cada movimiento posible, ponemos la jugada en un nuevo tablero para comprobar
            nuevo_estado = self.resultado(estado, posibles_movida) 
            puntuacion = self.alfabeta(nuevo_estado, otro_jugador) # de forma recursiva le mandamos el jugador humano para ver sus posibles jugadas
            # print(puntuacion['valor'])
            puntuacion['posicion'] = posibles_movida # ponemos cada posible movida

            if(jugador == max_jugador): # si esta jugando el humano
                if(puntuacion['valor'] > obj['valor']): # si la nueva puntuacion obtenida es mayor a la anterior puntucion 
                    obj = puntuacion # remplaza la nueva puntucion 
                # verificamos si hay un valor de 

            else: # si esta jugando la maquina
                if(puntuacion['valor'] < obj['valor']):
                    obj = puntuacion
            # return obj
        return obj
    
    # realiza el movimiento de la maquina
    def mover_computadora(self, estado):
        posicion = self.alfabeta(estado, self.letra)['posicion']
        return posicion

if __name__ == '__main__':
    juego = CuatroEnRaya()
    juego.iniciar()