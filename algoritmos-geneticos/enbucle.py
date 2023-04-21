from math import inf as infinity
from random import choice
import platform
import time
from os import system
import random

# Que valores debe tener X1, X2 y X3 para que y = 6
y_buscada = 6
# Ecuacion: y = x1 - 2 * X2 + 3 * X3

diferencia_minima_identificada = infinity
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0

for i in range(0, 100):
  for j in range(0, 100):
    for k in range(0, 100):
      y_hat = 3* i - 2 * j + 4 * k
      if (abs(y_hat - y_buscada) < diferencia_minima_identificada):
        print (f"x1: {i}, x2: {j}, x3: {k}, y_hat: {y_hat}, y_buscada: {y_buscada}, diferencia:{abs(y_hat - y_buscada)}")
        diferencia_minima_identificada = abs(y_hat - y_buscada)
        x1 = i
        x2 = j
        x3 = k
        if diferencia_minima_identificada == 0:
          break

print(f"La diferencia minima encontrada es: {diferencia_minima_identificada}")
print(f"con los valores de x1={x1}, x2={x2}, x3={x3}")

# Que valores debe tener X1, X2, X3, ..., x10 para que y = 6
y_buscada = 6
# Ecuacion: y = x1 - 2 * X2 + 3 * X3 - 5 * x4 + 1 * x5 - 12 * x6 - 4 * x7 + 2 * x8 - x9 + 3 * x10

# generamos un modelo para guardar cada valor de la ecuacion
class ModeloEcuacion:
  def __init__(self, dato_x, numero = 1):
        self.dato_x = dato_x
        self.numero = numero
  def get_dato_x(self):
    return self.dato_x
  
  def get_numero(self):
    return self.numero

# creamos un metodo para obtener los valores de la ecuacion
def get_ecuacion(numero):
  
  operaciones = []
  for caracter in numero:
    if caracter == '+' or caracter == '-':
        operaciones.append(caracter)
  
  lista = numero.split("+")  # separar por el caracter +
  items_con_multiplicacion = []
  for elemento in lista:
    sublista = elemento.split("-")  # separar cada elemento por el caracter -, y quitamos los espacios
    for items in sublista:
      items_con_multiplicacion.append(items.strip()) # agregamos y borramos los espacios
      

  if(len(operaciones) == len(items_con_multiplicacion)-1): # en una ecuacion el primer elemento no se espesifica la operacion por defecto es +
    operaciones.insert(0, '+')

  ecuacion_en_array = []
  cont = 0
  for elemento in items_con_multiplicacion:
    valores = elemento.split("*")
    el_numero = 1
    dato_x = None
    for num in valores:
      if(num.strip().isdigit()): # verificamos si el string es un numero
        el_numero = float(num)
        if(operaciones[cont] == '+'):
          el_numero = el_numero * +1
        else: el_numero = el_numero * -1
      else:
        dato_x = num.strip()
    
    modelo = ModeloEcuacion(dato_x, el_numero)
    ecuacion_en_array.append(modelo)
    cont += 1
    # print(modelo.get_dato_x(), modelo.get_numero())
  
  return ecuacion_en_array


ecuacion = get_ecuacion('x1 - 2 * X2 + 3 * X3 - 5 * x4 + 1 * x5 - 12 * x6 - 4 * x7 + 2 * x8 - x9 * 2')
# DEFINIMOS LA ECUACION
def funcion_adaptacion(individuo):
  y = 6
  # y_hat = 3 * individuo[0]  - 2 * individuo[1] + 4 * individuo[2]
#   y_hat = individuo[0] - 2 * individuo[1] + 3 * individuo[2] - 5 * individuo[3] + 1 * individuo[4] - 12 * individuo[5] 
#   - 4 * individuo[6] + 2 * individuo[7] - individuo[8] + 3 * individuo[9]
  y_hat = 0
  for i in range(1, len(individuo)-1):
    y_hat = y_hat + (individuo[i] * ecuacion[i].get_numero())
  
  return abs(y_hat - y)

def obtener_mejores_individuos(poblacion, numero_individuos, auxiliar):
  individuos_fitness = []
  mejor_fitness = infinity;
  for individuo in poblacion:
    fitness_individuo = funcion_adaptacion(individuo)
    individuos = []
    for i in range(auxiliar):
      individuos.append(individuo[i])

    individuos.append(fitness_individuo)
    # individuos_fitness.append([individuo[0], individuo[1], individuo[2],individuo[3], individuo[4], individuo[5],individuo[6], individuo[7], individuo[8], individuo[9], fitness_individuo])
    individuos_fitness.append(individuos)

  # print(individuos_fitness)
  individuos_fitness.sort(key=lambda x: x[auxiliar]) #sort metodo para ordenar en base a la posicion 10 son 11 elementos ahora
  
  return individuos_fitness[:numero_individuos]

def generar_individuos(numero_individuos, numero_genes):
  # Crear una lista vacía para almacenar todas las listas
  individuos = []

  # Crear 20 listas con 3 números aleatorios cada una
  for i in range(numero_individuos):
      cromosomas = []
      for j in range(numero_genes):
          nuevo_gen = random.randint(0, 9) # genera entre 0 y 9
          cromosomas.append(nuevo_gen)
      individuos.append(cromosomas)

  return individuos

def mostrar_individuos(poblacion):
  # Imprimir todas las listas generadas
  print(f"numero de individuos: {len(poblacion)}")
  for individuo in poblacion:
    print(individuo)

def generar_nuevos_individuos(mejores_individuos, auxiliar):
  nuevos_individuos =[]
#   hijo_1 = [
#     mejores_individuos[0][0],
#     mejores_individuos[0][1],
#     mejores_individuos[0][2],
#     mejores_individuos[0][3],
#     mejores_individuos[0][4],
#     mejores_individuos[len(mejores_individuos)-1][5], 
#     mejores_individuos[len(mejores_individuos)-1][6],
#     mejores_individuos[len(mejores_individuos)-1][7], 
#     mejores_individuos[len(mejores_individuos)-1][8], 
#     mejores_individuos[len(mejores_individuos)-1][9]
#     ]
  hijo_1 = []
  dividor = auxiliar/2 # como es 10 tomara el valor de 5
  for i in range(auxiliar):
      if(dividor < i): # mientras sea menor a 5
        hijo_1.append(mejores_individuos[0][i])
      else: 
        hijo_1.append(mejores_individuos[len(mejores_individuos)-1][i])
  nuevos_individuos.append(hijo_1)
#   hijo_2 = [
#     mejores_individuos[len(mejores_individuos)-1][0], 
#     mejores_individuos[len(mejores_individuos)-1][1], 
#     mejores_individuos[len(mejores_individuos)-1][2], 
#     mejores_individuos[len(mejores_individuos)-1][3], 
#     mejores_individuos[len(mejores_individuos)-1][4], 
#     mejores_individuos[0][5], 
#     mejores_individuos[0][6],
#     mejores_individuos[0][7], 
#     mejores_individuos[0][8], 
#     mejores_individuos[0][9]
#     ]
  hijo_2 = []
  for i in range(auxiliar):
      if(dividor < i): # mientras sea menor a 5
        hijo_2.append(mejores_individuos[len(mejores_individuos)-1][i])
      else: 
        hijo_2.append(mejores_individuos[0][i])
  nuevos_individuos.append(hijo_2)

  for numero_individuo in range(1, len(mejores_individuos)): 
    # hijo_1 = [
    #   mejores_individuos[numero_individuo - 1][0], 
    #   mejores_individuos[numero_individuo - 1][1], 
    #   mejores_individuos[numero_individuo - 1][2], 
    #   mejores_individuos[numero_individuo - 1][3], 
    #   mejores_individuos[numero_individuo - 1][4], 
    #   mejores_individuos[numero_individuo][5], 
    #   mejores_individuos[numero_individuo][6], 
    #   mejores_individuos[numero_individuo][7], 
    #   mejores_individuos[numero_individuo][8], 
    #   mejores_individuos[numero_individuo][9]
    #   ]
    hijo_1 = []
    for i in range(auxiliar):
      if(dividor < i): # mientras sea menor a 5
        hijo_1.append(mejores_individuos[numero_individuo - 1][i])
      else: 
        hijo_1.append(mejores_individuos[numero_individuo][i])
    nuevos_individuos.append(hijo_1)
    # hijo_2 = [
    #   mejores_individuos[numero_individuo][0], 
    #   mejores_individuos[numero_individuo][1], 
    #   mejores_individuos[numero_individuo][2], 
    #   mejores_individuos[numero_individuo][3], 
    #   mejores_individuos[numero_individuo][4], 
    #   mejores_individuos[numero_individuo - 1][5], 
    #   mejores_individuos[numero_individuo - 1][6], 
    #   mejores_individuos[numero_individuo - 1][7], 
    #   mejores_individuos[numero_individuo - 1][8], 
    #   mejores_individuos[numero_individuo - 1][9]
    #   ]
    hijo_2 = []
    for i in range(auxiliar):
      if(dividor < i): # mientras sea menor a 5
        hijo_2.append(mejores_individuos[numero_individuo][i])
      else: 
        hijo_2.append(mejores_individuos[numero_individuo - 1][i])
    nuevos_individuos.append(hijo_2)

  return nuevos_individuos

def main():
  auxiliar = len(ecuacion)
  poblacion = generar_individuos(100, auxiliar) # genera una matriz de 100 * 10
  mostrar_individuos(poblacion) # mostramos la matriz generada
  mejores_individuos = obtener_mejores_individuos(poblacion, 50, auxiliar) # genera individuo fitnes y devualve ordenado en base el fitnes
  mostrar_individuos(mejores_individuos)
  
  
  while(mejores_individuos[0][0] != 0):
    mejores_individuos_sin_fitness = [fila[:auxiliar] for fila in mejores_individuos] # elimina el elemento fitnes
    # mostrar_individuos(mejores_individuos_sin_fitness)

  

  nueva_poblacion = generar_nuevos_individuos(mejores_individuos, auxiliar) # genera una nueva poblacion
  poblacion = nueva_poblacion
  mostrar_individuos(poblacion) 
  mejores_individuos = obtener_mejores_individuos(poblacion, 50, auxiliar)
  mostrar_individuos(mejores_individuos)

if __name__ == '__main__':
    main()
    # get_ecuacion('x1 - 2 * X2 + 3 * X3 - 5 * x4 + 1 * x5 - 12 * x6 - 4 * x7 + 2 * x8 - x9 + 3 * x10')