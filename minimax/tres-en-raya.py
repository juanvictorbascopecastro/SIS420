import random
import os
import math

class TresEnRaya:
    def __init__(self):
        # self.tablero = ['-' for i in range(9)]
        self.tablero = []
        for i in range(9):
            self.tablero.append(' ')
        self.humano = 'X'
        self.coputadora = 'O'
        # if random.randint(0, 1) == 1: # si es 1 X sera el humano
        #     self.humano = 'X'
        #     self.coputadora = 'O'
        # else: # si no O sera el humano
        #     self.humano = 'O'
        #     self.coputadora = 'X'

    # def get_tablero(self): return self.tablero
    # muestra el trablero 
    def ver_trablero(self): 
        print("")
        for i in range(3):
            print(" ", self.tablero[0+(i*3)], ' | ', self.tablero[1+(i*3)], ' | ', self.tablero[2+(i*3)], " ")
            if(i != 2): print("-----------------")

    def tablero_lleno(self, estado):
        return not ' ' in estado
    
    def hay_ganador(self, estado, jugador):
        if estado[0] == estado[1] == estado[2] == jugador: return True
        if estado[3] == estado[4] == estado[5] == jugador: return True
        if estado[6] == estado[7] == estado[8] == jugador: return True

        if estado[0] == estado[3] == estado[6] == jugador: return True
        if estado[1] == estado[4] == estado[7] == jugador: return True
        if estado[2] == estado[5] == estado[8] == jugador: return True

        if estado[0] == estado[4] == estado[8] == jugador: return True
        if estado[2] == estado[4] == estado[6] == jugador: return True
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
    
    def iniciar(self):
        jugador_humano = jugadorHumano(self.humano)
        jugador_computadora = jugadorComputador(self.coputadora)

        while True:
            os.system('cls') # limpiar consola
            print(" Turno de ", self.humano)
            self.ver_trablero()

            # pone su jugada el humano
            posicion = jugador_humano.mover_humano(self.tablero)
            self.tablero[posicion] = self.humano
            if(self.si_el_juego_acabo()): 
                self.ver_trablero()
                break
            # pone su jugada el computador
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
            posicion = int(input("Ingresa tu movida entre [1-9]: "))
            print()
            # en caso de que no volvera a preguntar
            if(estado[posicion-1] == ' ' and posicion > 0 and posicion < 10): # si la casilla esta vacia ponemos su jugada
                break
        return posicion - 1 

# hace su jugada el computador
class jugadorComputador(TresEnRaya): #hereda de la clase TresEnRaya
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
    
    def minimax(self, estado, jugador):
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
        
        for posibles_movida in self.acciones(estado): # recorremos todas las movidas posib;e
            # por cada movimiento posible, ponemos la jugada en un nuevo tablero para comprobar
            nuevo_estado = self.resultado(estado, posibles_movida) 
            puntuacion = self.minimax(nuevo_estado, otro_jugador) # de forma recursiva le mandamos el jugador humano para ver sus posibles jugadas
            puntuacion['posicion'] = posibles_movida # ponemos cada posible movida

            if(jugador == max_jugador): # si esta jugando el humano
                if(puntuacion['valor'] > obj['valor']): # si la nueva puntuacion obtenida es mayor a la anterior puntucion 
                    obj = puntuacion # remplaza la nueva puntucion 
            else: # si esta jugando la maquina
                if(puntuacion['valor'] < obj['valor']):
                    obj = puntuacion
                    # print('maquina',puntuacion['valor'])
            
        return obj
    
    # realiza el movimiento de la maquina
    def mover_computadora(self, estado):
        posicion = self.minimax(estado, self.letra)['posicion']
        return posicion

if __name__ == '__main__':
    juego = TresEnRaya()
    juego.iniciar()