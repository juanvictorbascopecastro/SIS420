import math

superficie = [150, 200, 500, 550, 320, 300, 800, 210, 180, 350] # x
precios = [45000, 120000, 130000, 350000, 190000, 160000, 200000, 50000, 75000, 210000] # y

resultado = []
for i, x in enumerate(superficie):
    mejor_diferencia = math.inf
    mejor_a = 0
    mejor_b = 0
    for a in range(-10000, 10, 10000):
        for b in range(-10000, 10, 10000):
            y_hat = a + b * x # x son las superficies  y la y son los precios
            # print(y_hat, '=', b, '+', b, '*', x)
            diferencia_actual = (y_hat - precios[i])
            if(diferencia_actual < mejor_diferencia):
                mejor_diferencia = diferencia_actual
                mejor_a = a
                mejor_b = b

    resultado.append({
                    'diferencia': mejor_diferencia,
                    'a': mejor_a,
                    'b': mejor_b
                })         
    print(f'Los mejores coeficiente en la ecuacion de la linea recta para x{i+1} =', x , '| a =' , resultado[i]['a'] , '| b =', resultado[i]['b'])

promedio_a = sum([ca['a'] for ca in resultado]) / len(resultado)
promedio_b = sum([cb['b'] for cb in resultado]) / len(resultado)

print(f'Promedio a = {promedio_a}; b = {promedio_b}')
