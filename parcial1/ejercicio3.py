"""
EJERCICIO 3
Desarrolle un algoritmo genético que permita generar una contraseña de 9 dígitos numéricos
donde la secuencia de pulsación considere la máxima distancia entre las teclas presionadas, 
es decir evitar en lo posible que se presionen teclas aledañas.
Generar llaves, claves, las teclas que preciones deben estar alejadas
"""
import random
tamano_poblacion = 100
numero_genes = 5
probabilidad_mutacion = 0.5

# genera claves entre 1 y 9
def generar_poblacion(tamano_poblacion):
    poblacion = []
    for i in range(tamano_poblacion):
        individuo = ''.join([str(random.randint(1, 9)) for _ in range(9)]) # generar una cadena de 9 dígitos aleatorios
        poblacion.append(individuo)
    return poblacion
    
def seleccionar_padres(poblacion):
    # seleccionamos 2 individuos aleatorios de la población
    posicion1 = random.randint(0, len(poblacion)-1)
    posicion2 = random.randint(0, len(poblacion)-1)
    padre1 = poblacion[posicion1]
    padre2 = poblacion[posicion2]
    # evaluamos la aptitud de ambos individuos 
    aptitud1 = evaluar_aptitud(padre1)
    aptitud2 = evaluar_aptitud(padre2)
    # print(aptitud1)
    # print(aptitud2)
    if aptitud1 > aptitud2: # retorna el que tiene mayor diferencia
        return padre1
    else:
        return padre2
    
    # aptitud = 0
    # padre = []
    # for i in range(tamano_poblacion-1):
    #     nueva_aptitud = evaluar_aptitud(poblacion[i])
    #     if (nueva_aptitud > aptitud): 
    #         aptitud = nueva_aptitud
    #         padre = poblacion[i]
    
    # return padre
    
def cruzar_padres(padre1, padre2):
    # elegimos un punto de cruce aleatorio
    punto_cruce = random.randint(1, 7) # se elije 1 y 7 para asegurar que siempre haya combinaciones como la logitud es 0 y 8
    # punto_cruce = 4
    # print(padre1, punto_cruce, padre1[:punto_cruce], padre1[:punto_cruce] + padre2[punto_cruce:])
    # combinamos las partes de los padres antes y después del punto de cruce
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:] # obtiene la subcadena y combina con la otra cadena del padre
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    # retornamos los 2 hijos generados
    return hijo1, hijo2

def evaluar_aptitud(individuo):
    suma_distancias = 0
    for i in range(7):
        suma_distancias = suma_distancias + abs(int(individuo[i]) - int(individuo[i+1])) # calculamos la suma de las distancias entre dígitos adyacentes
    # print(suma_distancias)
    return suma_distancias


def aplicar_mutacion(individuo):
    # convertimos el individuo a lista para poder modificarlo
    lista_individuo = list(individuo)
    for i in range(9): # recorremos cada dígito del individuo
        if random.random() < probabilidad_mutacion: # generamos un número aleatorio para determinar si se realiza la mutación 
            # para generar un digito diferente al actual
            numeros = ['1','2','3','4','5','6','7','8','9'] # tenemos un vector con los numeros         
            while True: # obtenemos un numero random
                nuevo_digito = numeros[random.randint(0, len(numeros)-1)] # generamos un aleatorio para obtener su posicion
                if(nuevo_digito != lista_individuo[i]): break

            # nuevo_digito = random.choice([x for x in '123456789' if x != lista_individuo[i]])
            # reemplazamos el dígito actual por el nuevo dígito
            lista_individuo[i] = nuevo_digito
    # convertimos la lista de nuevo a cadena y retornamos el individuo mutado
    return ''.join(lista_individuo)

# función para evolucionar una los genes
def evolucionar_genes(poblacion):
    # seleccionamos los padres para generar los nuevos individuos
    nuevos_individuos = []
    for i in range(tamano_poblacion):
        padre1 = seleccionar_padres(poblacion)
        padre2 = seleccionar_padres(poblacion)
        # realizamos el cruce entre los 2 padres para generar 2 hijos
        hijo1, hijo2 = cruzar_padres(padre1, padre2)
        # aplicamos mutaciones a los 2 hijos
        hijo1_mutado = aplicar_mutacion(hijo1)
        hijo2_mutado = aplicar_mutacion(hijo2)
        # agregamos los 2 hijos mutados a la lista de nuevos individuos
        nuevos_individuos.append(hijo1_mutado)
        nuevos_individuos.append(hijo2_mutado)

    # evaluamos la aptitud de los nuevos individuos y lo guardamos en un array
    aptitudes = [evaluar_aptitud(individuo) for individuo in nuevos_individuos]
    # seleccionamos los mejores individuos para formar la siguiente generación
    lista_diccionario = []
    for i in range(tamano_poblacion):
        item = { 'valor': nuevos_individuos[i], 'aptitud': aptitudes[i] } # creamos un objeto
        lista_diccionario.append(item)
        
    lista_diccionario.sort(key=lambda x: x['aptitud']) # ordenamos en base a la aptitud
    lista_diccionario = sorted(lista_diccionario, key=lambda x: x['aptitud'], reverse=True) # invierte el arreglo
    nueva_lista = [diccionario['valor'] for diccionario in lista_diccionario]
    poblacion = [individuo for individuo in nueva_lista][:tamano_poblacion] # obtenemos los primeros 100 de las aptitudes evaluadas
    return poblacion
    # poblacion = [individuo for _, individuo in sorted(zip(aptitudes, nuevos_individuos), reverse=True)][:tamano_poblacion]
    # return poblacion

if __name__ == "__main__":
    # teclas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    poblacion = poblacion = generar_poblacion(tamano_poblacion)
    # evolucionamos la población durante el número de generaciones especificado
    for i in range(numero_genes):
        print(poblacion)
        poblacion = evolucionar_genes(poblacion)
        # imprimimos la clave más apta de la generación actual
        print('generacion', i+1, '- contraseña mas apta:', poblacion[0])
    # retornamos la clave más apta encontrada
    print('contraseña generada', poblacion[0])