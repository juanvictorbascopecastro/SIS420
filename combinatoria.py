'INTERCAMBIAR DOS FICHAS SEGUIDAS DESDE UNA BASE HASTA HALLAR UNA COMBINACION'
'EN ESTRUCTURA DE ARBOL'

inicio = [3, 2, 0, 1] # BASE
fin = [0, 1, 2, 3] # FNAL

resultados = []

def esIgual(arr1, arr2): 
    if(len(arr1) != len(arr2)): return False
    for i, item in enumerate(arr1):
        if(arr1[i] != arr2[i]): return False  
    return True

def combinar(arr): 
    result = [arr[1], arr[0], arr[2], arr[3]]
    print(result)
    resultados.append(result)
    if(esIgual(result, fin)): return True

    result = [arr[0], arr[2], arr[1], arr[3]]
    print(result)
    resultados.append(result)
    if(esIgual(result, fin)): return True
    
    result = [arr[0], arr[1], arr[3], arr[2]]
    print(result)
    resultados.append(result)
    if(esIgual(result, fin)): return True    
    return False

existe = combinar(inicio)
contador_rama = len(inicio) - 1
cont = 0
while (existe == False):
    while (cont < contador_rama and existe == False):
        print("Base: ", cont);
        existe = combinar(resultados[cont]);
        cont = cont + 1
    
    contador_rama = contador_rama + len(inicio) - 1;

print('===================== ENCONTRADO EN LA ITERACION', len(resultados), ' ============================')
