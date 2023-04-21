import random
from math import inf as infinity

#Alunos:
#Caique de Paula Figueiredo Coelho
#Lucas Queiroz
def getBoardCopy(board):
	# Hace una copia del tablero y devuélveme esta copia

	duplicateBoard = []

	for i in board:
		duplicateBoard.append(i)

	return duplicateBoard

def imprimirTablero(board):
	# Esta función imprime el tablero del juego.
  	# El marco es una lista de 9 cadenas que representan el tablero	
	print(board)
	copyBoard = getBoardCopy(board)
	
	
	for i in range(1,37):
		if(board[i] == ''):
			copyBoard[i] = str(i)
		else:
			copyBoard[i] = board[i]
	
	print(' ' + copyBoard[31] + '|' + copyBoard[32] + '|' + copyBoard[33] + '|' + copyBoard[34]+ '|' + copyBoard[35]+ '|' + copyBoard[36])
	#print(' | |')
	print('-----------------')
	#print(' | |')
	print(' '+ copyBoard[25] + '|' + copyBoard[26] + '|' + copyBoard[27]+ '|' + copyBoard[28]+ '|' + copyBoard[29]+ '|' + copyBoard[30])
	#print(' | |')
	print('-----------------')
	#print(' | |')
	print(' '+ copyBoard[19] + '|' + copyBoard[20] + '|' + copyBoard[21]+ '|' + copyBoard[22]+ '|' + copyBoard[23]+ '|' + copyBoard[24])
	#print(' | |')
	print('-----------------')
	#print(' | |')
	print(' '+ copyBoard[13] + '|' + copyBoard[14] + '|' + copyBoard[15]+ '|' + copyBoard[16]+ '|' + copyBoard[17]+ '|' + copyBoard[18])
	print('-----------------')
	#print(' | |')
	print(' '+ copyBoard[7] + ' |' + copyBoard[8] + ' |' + copyBoard[9]+ ' |' + copyBoard[10]+ '|' + copyBoard[11]+ '|' + copyBoard[12])
	print('-----------------')
	#print(' | |')
	print(' '+ copyBoard[1] + ' |' + copyBoard[2] + ' |' + copyBoard[3]+ ' |' + copyBoard[4]+ ' |' + copyBoard[5]+ ' |' + copyBoard[6])
	print('-----------------')
	#print(' | |')

def inputPlayerLetter():
	# El jugador elige con qué letra quiere jugar "X" u "O" 
  # Devuelve una lista con la letra del jugador y la letra de la computadora

	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Usted quiere ser X o O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("¡Solo ingresa la letra X si quieres ser X o la letra O si quieres ser O!")

	#El primer elemento de la lista es el jugador humano y el segundo es la computadora.
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def quienJuegaPrimero():
	# return 'computador'
	#Elige al azar al jugador que jugará primero
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'humano'

def marcarMovimiento(board, letter, move):
	#Hace el movimiento de la computadora o del jugador dependiendo de la letra en el tablero
	board[move] = letter

def siEsGanador(board, letter):
	#Dado un cuadrado y una letra, esta función devuelve True si la letra dada gana el juego.
	return(
		# horizontal
		(board[1] == letter and board[2] == letter and board[3] == letter and board[4] == letter) or
		(board[2] == letter and board[3] == letter and board[4] == letter and board[5] == letter) or
		(board[3] == letter and board[4] == letter and board[5] == letter and board[6] == letter) or
		
		(board[7] == letter and board[8] == letter and board[9] == letter and board[10] == letter) or
		(board[8] == letter and board[9] == letter and board[10] == letter and board[11] == letter) or
		(board[9] == letter and board[10] == letter and board[11] == letter and board[12] == letter) or

		(board[13] == letter and board[14] == letter and board[15] == letter and board[16] == letter) or
		(board[14] == letter and board[15] == letter and board[16] == letter and board[17] == letter) or
		(board[15] == letter and board[16] == letter and board[17] == letter and board[18] == letter) or

		(board[19] == letter and board[20] == letter and board[21] == letter and board[22] == letter) or
		(board[20] == letter and board[21] == letter and board[22] == letter and board[23] == letter) or
		(board[21] == letter and board[22] == letter and board[23] == letter and board[24] == letter) or

		(board[25] == letter and board[26] == letter and board[27] == letter and board[28] == letter) or
		(board[26] == letter and board[27] == letter and board[28] == letter and board[29] == letter) or
		(board[27] == letter and board[28] == letter and board[29] == letter and board[30] == letter) or

		(board[31] == letter and board[32] == letter and board[33] == letter and board[34] == letter) or
		(board[32] == letter and board[33] == letter and board[34] == letter and board[35] == letter) or
		(board[33] == letter and board[34] == letter and board[35] == letter and board[36] == letter) or

		# vertical
		(board[1] == letter and board[7] == letter and board[13] == letter and board[19] == letter) or
		(board[7] == letter and board[13] == letter and board[19] == letter and board[25] == letter) or
		(board[13] == letter and board[19] == letter and board[25] == letter and board[31] == letter) or

		(board[2] == letter and board[8] == letter and board[14] == letter and board[20] == letter) or
		(board[8] == letter and board[14] == letter and board[20] == letter and board[26] == letter) or
		(board[14] == letter and board[20] == letter and board[26] == letter and board[32] == letter) or

		(board[3] == letter and board[9] == letter and board[15] == letter and board[21] == letter) or
		(board[9] == letter and board[15] == letter and board[21] == letter and board[27] == letter) or
		(board[15] == letter and board[21] == letter and board[27] == letter and board[33] == letter) or

		(board[4] == letter and board[10] == letter and board[16] == letter and board[22] == letter) or
		(board[10] == letter and board[16] == letter and board[22] == letter and board[28] == letter) or
		(board[16] == letter and board[22] == letter and board[28] == letter and board[34] == letter) or

		(board[5] == letter and board[11] == letter and board[17] == letter and board[23] == letter) or
		(board[11] == letter and board[17] == letter and board[23] == letter and board[29] == letter) or
		(board[17] == letter and board[23] == letter and board[29] == letter and board[35] == letter) or

		(board[6] == letter and board[12] == letter and board[18] == letter and board[24] == letter) or
		(board[12] == letter and board[18] == letter and board[24] == letter and board[30] == letter) or
		(board[18] == letter and board[24] == letter and board[30] == letter and board[36] == letter) or
		# diagonales
		(board[19] == letter and board[14] == letter and board[9] == letter and board[4] == letter) or
		(board[25] == letter and board[20] == letter and board[15] == letter and board[10] == letter) or
		(board[20] == letter and board[15] == letter and board[10] == letter and board[5] == letter) or
		(board[31] == letter and board[26] == letter and board[21] == letter and board[16] == letter) or
		(board[26] == letter and board[21] == letter and board[16] == letter and board[11] == letter) or
		(board[21] == letter and board[16] == letter and board[11] == letter and board[6] == letter) or
		(board[32] == letter and board[27] == letter and board[22] == letter and board[17] == letter) or
		(board[27] == letter and board[22] == letter and board[17] == letter and board[12] == letter) or
		(board[33] == letter and board[28] == letter and board[23] == letter and board[18] == letter) or

		(board[13] == letter and board[20] == letter and board[27] == letter and board[24] == letter) or
		(board[7] == letter and board[14] == letter and board[21] == letter and board[28] == letter) or
		(board[14] == letter and board[21] == letter and board[28] == letter and board[35] == letter) or
		(board[1] == letter and board[8] == letter and board[15] == letter and board[22] == letter) or
		(board[8] == letter and board[15] == letter and board[22] == letter and board[29] == letter) or
		(board[15] == letter and board[22] == letter and board[29] == letter and board[36] == letter) or
		(board[2] == letter and board[9] == letter and board[16] == letter and board[23] == letter) or
		(board[9] == letter and board[16] == letter and board[23] == letter and board[30] == letter) or
		(board[3] == letter and board[10] == letter and board[17] == letter and board[24] == letter))
		# (board[7] == letter and board[8] == letter and board[9] == letter) or #linea superior
		# (board[4] == letter and board[5] == letter and board[6] == letter) or #linea del medio
		# (board[1] == letter and board[2] == letter and board[3] == letter) or #linea de abajo
		# (board[7] == letter and board[4] == letter and board[1] == letter) or #columna de la izquierda
		# (board[8] == letter and board[5] == letter and board[2] == letter) or #columna del medio
		# (board[9] == letter and board[6] == letter and board[3] == letter) or #columna da la derecha

		# (board[7] == letter and board[5] == letter and board[3] == letter) or #diagonal principal
		# (board[9] == letter and board[5] == letter and board[1] == letter)) #diagonal secundaria

def esEspacioLibre(board, move):
	# Devuelve verdadero si el espacio solicitado está libre en el tablero
	if(board[move] == ''):
		return True
	else:
		return False

def getPlayerMove(board):
	# Recibe el movimiento del jugador
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'.split() or not esEspacioLibre(board, int(move)):
		print('Cual es su proximo movimiento? (1-36)')
		move = input();
		if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'):
			print("MOVIMENTO INVALIDO! INTRODUSCA UN NUMERO ENTRE 1 Y 36!")
		
		if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36'):
			if(not esEspacioLibre(board, int(move))):
				print("ESPACIO NO DISPONIBLE! ELIJA OTRO ESPACO ENTRE 1 Y 9 O CUALQUIER NUMERO DISPONIBLE EN EL TABLERO!")

	return int(move)
 
def chooseRandomMoveFromList(board, movesList):
  # Devuelve un movimiento aleatorio válido
  # Devuelve None si no hay movimientos válidos

	possiveisMovimentos = []
	for i in movesList:
		if esEspacioLibre(board, i):
			possiveisMovimentos.append(i)

	if len(possiveisMovimentos) != 0:
		return random.choice(possiveisMovimentos)
	else:
		return None

def isBoardFull(board):
	# Devuelve True si todos los espacios de tablero no están disponibles
	for i in range(1, 37):
		if esEspacioLibre(board, i):
			return False
	return True

def possiveisOpcoes(board):
	# Devuelve una lista de todos los espacios en el tablero que están disponibles

	opcoes = []

	for i in range(1, 37):
		if esEspacioLibre(board, i):
			opcoes.append(i)

	return opcoes

def finishGame(board, computerLetter):
	#Verifica se o jogo chegou ao final
	#Retorna -1 se o jogador ganha
	#Retorna 1 se o computador ganha
	#Retorna 0 se o jogo termina empatado
	#Retorna None se o jogo nao terminou

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if(siEsGanador(board, computerLetter)):
		return 1

	elif(siEsGanador(board, playerLetter)):
		return -1

	elif(isBoardFull(board)):
		return 0

	else:
		return None


def alphabeta(board, computerLetter, turn, alpha, beta):
	#Fazemos aqui a poda alphabeta
	#print(board, turn, alpha, beta)

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = finishGame(board, computerLetter)

	if (finish != None):
		return finish

	possiveis = possiveisOpcoes(board) # posibles marcaciones
	if turn == computerLetter: # si es el valor de la computadora
		for move in possiveis:
			marcarMovimiento(board, turn, move)
			# print(board, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			marcarMovimiento(board, '', move)
			# print(val)
			# print(val, '>', alpha)

			# # alfa = -2 beta = 2
			# exit()
			if val > alpha:		
				alpha = val

			if alpha >= beta:
				return alpha
		return alpha

	else: # si es el valor del humano
		for move in possiveis:
			marcarMovimiento(board, turn, move)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta)
			marcarMovimiento(board, '', move)
			if val < beta:
				beta = val

			if alpha >= beta:
				return beta
		return beta



def getComputerMove(board, turn, computerLetter):
	#Definimos aquí cuál será el movimiento del ordenador
	a = -2
	opcoes = []

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	#if len(possiveisOpcoes(board)) == 9:
	#	return 5

	#Comecamos aqui o MiniMax
	#Primeiro chechamos se podemos ganhar no proximo movimento
	for i in range(1, 37):
		copy = getBoardCopy(board) # hace una copia
		if esEspacioLibre(copy, i):
			marcarMovimiento(copy, computerLetter, i)
			if siEsGanador(copy, computerLetter):
				return i

	#Checa se o jogador pode vencer no proximo movimento e bloqueia
	for i in range(1, 37):
		copy = getBoardCopy(board)
		if esEspacioLibre(copy, i):
			marcarMovimiento(copy, playerLetter, i)
			if siEsGanador(copy, playerLetter):
				return i

	possiveisOpcoesOn = possiveisOpcoes(board) # obtiene todos los espacios libre

	# print(possiveisOpcoesOn)
	for move in possiveisOpcoesOn:
		marcarMovimiento(board, computerLetter, move)
		# val = alphabeta(board, computerLetter, playerLetter, -infinity, infinity)	
		val = alphabeta(board, computerLetter, playerLetter, -2, 2)	
		print(val)	
		marcarMovimiento(board, '', move)

		if val > a:
			a = val
			opcoes = [move]                                                                                                                    

		elif val == a:
			opcoes.append(move)

	return random.choice(opcoes)

print('¡Juguemos el juego de 3 en raya!')

jogar = True

while jogar:
	#Restablecer el juego
	theBoard = [''] * 37
	# os.system('cls')
	playerLetter, computerLetter = inputPlayerLetter()
	turn = quienJuegaPrimero() # quien juega primero
	print(turn +' juega primero,')
	gameisPlaying = True

	while gameisPlaying:
		if turn == 'humano': # tu juegas primero
			imprimirTablero(theBoard)
			move = getPlayerMove(theBoard) # valida el movimiento marcado
			marcarMovimiento(theBoard, playerLetter, move)

			if siEsGanador(theBoard, playerLetter):
				imprimirTablero(theBoard)
				print('Woooow! Ganaste el juego!')
				gameisPlaying = False
			
			else:
				if isBoardFull(theBoard):
					imprimirTablero(theBoard)
					print('O El juego terminó en empate')
					break
				else:
					turn = 'computador'

		else: # la computadora juega
			move = getComputerMove(theBoard, playerLetter, computerLetter)
			print(move)
			marcarMovimiento(theBoard, computerLetter, move)

			if siEsGanador(theBoard, computerLetter): # si es ganador
				imprimirTablero(theBoard)
				print("O Computadora gano :(")
				gameisPlaying = False

			else: # 
				if isBoardFull(theBoard): # si hay espacios disponibles
					imprimirTablero(theBoard)
					print('O El juego terminó en empate')
					break
				else:
					turn = 'humano'

	letterNew = ''
	while not(letterNew == 'S' or letterNew == 'N'):
		print("¿Quieres volver a jugar? Tipo S (para sí) o N (para no)")
		letterNew = input().upper()
		if (letterNew != 'S' and letterNew != 'N'):
			print("¡Entrada no válida! ¡Escriba S (para sí) o N (para no)!")
		if(letterNew == 'N'):
			print("¡Fue bueno jugar contigo! ¡Nos vemos luego!")
			jogar = False

