import random
import math
  
numero_genes = 5 #La longitud del material genetico de cada individuo
tamano_poblacion = 100 #La cantidad de individuos que habra en la poblacion
precision = 30 #Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
probabilidad_mutacion = 0.4 #La probabilidad de que un individuo mute
valor_minimo_gen = -10
valor_maximo_gen = 10

def crear_individuo(min, max):
    # Crea un individuo
    
    # cromosoma = []
    # for i in range(numero_genes):
    #   cromosoma.append(random.randint(min, max))
    
    # return cromosoma

    return[random.randint(min, max) for i in range(numero_genes)]

# print(crear_individuo(-10, 10))

def crear_poblacion(numero_individuos):
    # Crea una poblacion nueva de individuos
    
    return [crear_individuo(valor_minimo_gen, valor_maximo_gen) for i in range(numero_individuos)]

# poblacion_prueba = crear_poblacion(10)
# print(poblacion_prueba)

def calcular_fitness(individuo):
    # Calcula el fitness de un individuo concreto.
    # F(x) = 2*x1 + 5*x2^2 - x3 + x4 - 8 * x5 - 10
    # print(individuo)
    Fx = abs(2 * individuo[0] + 5 * individuo[1]**2 - individuo[2] + individuo[3] -8 * individuo[4] - 10)
    
    return Fx

# print(calcular_fitness(poblacion_prueba[0]))

# funcion empleada para ordenar la poblacion
def ordenar_por_segundo_elemento(elem):
    return elem[1]   

# poblacion = crear_poblacion(tamano_poblacion)
# poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
# poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)
# poblacion = [i[0] for i in poblacion_ordenada]

# for ind in poblacion_ordenada:
#   print(f"individuo: {ind[0]} fitness: {ind[1]}")

# print("###"*3)

# for ind in poblacion:
#   print(f"individuo: {ind} fitness: {calcular_fitness(ind)}")

def seleccion_y_reproduccion(poblacion):
  # Puntua todos los elementos de la poblacion (population) y se queda con los mejores guardandolos dentro de 'seleccionados'.
  # Despues mezcla el material genetico de los elegidos para crear nuevos individuos y llenar la poblacion 
  # (guardando tambien una copia de los individuos seleccionados sin modificar).
  # Por ultimo se aplica la mutacion a los individuos.
  poblacion_evaluada = [(indiv, calcular_fitness(indiv)) for indiv in poblacion ] #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (5 , [1,2,1,1,4,1,8,9,4,1])
  poblacion_ordenada  = [indiv[0] for indiv in sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)] #Ordena los pares ordenados y se queda solo con el array de valores
  
  poblacion = poblacion_ordenada
  #poblacion_seleccionada = poblacion_ordenada[(len(poblacion_ordenada) - precision):] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
  poblacion_seleccionada = poblacion_ordenada[precision:] #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'precision'
  #Se mezcla el material genetico para crear nuevos individuos
  for i in range(precision, len(poblacion)):
    punto_cruce = random.randint(1, numero_genes - 1) #Se elige un punto para hacer el intercambio
    padre = random.sample(poblacion_seleccionada, 2) #Se eligen dos padres
    poblacion[i][:punto_cruce] = padre[0][:punto_cruce] #Se mezcla el material genetico de los padres en cada nuevo individuo
    poblacion[i][punto_cruce:] = padre[1][punto_cruce:]
  
  return poblacion #El array 'poblacion' tiene ahora una nueva poblacion de individuos, que se devuelven

poblacion = crear_poblacion(tamano_poblacion)
poblacion = seleccion_y_reproduccion(poblacion)
poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)
poblacion = [i[0] for i in poblacion_ordenada]

for ind in poblacion_ordenada:
  print(f"individuo: {ind[0]} fitness: {ind[1]}")


def mutacion(poblacion):
  #Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podriavalcanzarse la solucion.
   
  for i in range(precision, len(poblacion)):
    if random.random() <= probabilidad_mutacion: #Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
      punto = random.randint(0, numero_genes - 1) #Se elgie un punto al azar
      nuevo_valor = random.randint(valor_minimo_gen, valor_maximo_gen) #y un nuevo valor para este punto
  
      #Es importante mirar que el nuevo valor no sea igual al viejo
      while nuevo_valor == poblacion[i][punto]:
          nuevo_valor = random.randint(valor_minimo_gen, valor_maximo_gen)
  
      #Se aplica la mutacion
      poblacion[i][punto] = nuevo_valor
  
  return poblacion


poblacion = crear_poblacion(tamano_poblacion)#Inicializar una poblacion
print("Poblacion Inicial:") #Se muestra la poblacion inicial
poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

for ind in poblacion_ordenada:
  print(f"individuo: {ind[0]} fitness: {ind[1]}")

numero_generaciones = 1000
mejor_fitness = 10000
numero_generacion = 0;
break_out_flag = False
#Se evoluciona la poblacion
for i in range(numero_generaciones):
    puntuados = [ (ind, calcular_fitness(ind)) for ind in poblacion] 
    numero_generacion = numero_generacion + 1
    for indPun in puntuados:
      if indPun[1] < mejor_fitness:
        mejor_fitness = indPun[1]
      if indPun[1] == 0:
        break_out_flag = True
        break

    if break_out_flag:
        break

    poblacion = seleccion_y_reproduccion(poblacion)
    poblacion = mutacion(poblacion)

    poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
    poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

    print(f"generacion no: {numero_generacion}")
    for ind in poblacion_ordenada:
      print(f"individuo: {ind[0]} fitness: {ind[1]}")


print("Poblacion final:")

poblacion_evaluada = [(i, calcular_fitness(i)) for i in poblacion ]
poblacion_ordenada  = sorted(poblacion_evaluada, key=ordenar_por_segundo_elemento)

for ind in poblacion_ordenada:
  print(f"individuo: {ind[0]} fitness: {ind[1]}")

# print("\nPoblacion Final que cuenta con una solucion:\n%s"%(poblacion)) #Se muestra la poblacion evolucionada
# print("\n\n")

if mejor_fitness == 0:
  individuo = poblacion_ordenada[0][0]
  print(f"El mejor fenotipo que resuelve la ecuacion es:{individuo}")
  print(f"La solucion a la ecuacion 2X1 + 5X2² - X3 + X4 - 8X5 - 10 = 0 es {2 * individuo[0]} + {5 * individuo[1]**2} - {individuo[2]} + {individuo[3]} - {8 * individuo[4]} -10 = 0")
  print(f"la solucion se encontro en la {numero_generacion} generación")
else:
  print("El algoritmo no pudo encontrar una solucion")

