estado_inicial = [3, 2, 0, 1]
estado_objetivo = [0, 1, 2, 3]

def generar_nuevos_estados(estado_inicial):
  nuevo_estado_1 = [estado_inicial[1], estado_inicial[0], estado_inicial[2], estado_inicial[3]]
  nuevo_estado_2 = [estado_inicial[0], estado_inicial[2], estado_inicial[1], estado_inicial[3]]
  nuevo_estado_3 = [estado_inicial[0], estado_inicial[1], estado_inicial[3], estado_inicial[2]]

  nuevos_estados = []
  nuevos_estados.append(nuevo_estado_1)
  nuevos_estados.append(nuevo_estado_2)
  nuevos_estados.append(nuevo_estado_3)
  return nuevos_estados


estados_frontera = []
estados_revisados = []
estados_frontera.extend([estado_inicial])
estado_actual = estado_inicial

while(estado_actual != estado_objetivo and len(estados_frontera) > 0):
  aux_estados = generar_nuevos_estados(estado_actual)
  estados_frontera.extend(aux_estados)
  estados_revisados.append(estado_actual)
  print("ESTADOS FRONTERA")
  print(estados_frontera)
  estado_actual = estados_frontera.pop(0)
  while estado_actual in estados_revisados:
    estado_actual = estados_frontera.pop(0)
  
  
  print("ESTADOS REVISADOS")
  print(estados_revisados)
