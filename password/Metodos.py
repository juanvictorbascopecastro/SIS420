import random
class Metodos:
    
    def logitudIguales(arr1, arr2):
        cont = 0
        valores = 0
        while(cont < len(arr1)):
            cont2 = 0
            while(cont2 < len(arr2)):
                if(arr1[cont] == arr2[cont2]):
                    valores +=1
                    cont2 = len(arr2) # para salir del bucle
                cont2 += 1
            cont += 1
        if(valores >= len(arr1)): return True
        else: return False

    def generRandon(arr1, size): 
        #debemos obtener el numero minimo de la contrasenia
        min = arr1[0]
        for i in range(0, size):
            if(arr1[i] < min): min = arr1[i]
        return random.sample(range(min,size+min),size)
    