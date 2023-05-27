# python -m pip install --user pandas
# utilizado para manejos de directorios y rutas
import os
import pandas as pd # permite leer archivo excel
import numpy as np # permite leer archivos txt

class LeerArchivo:
    def leerTxt(nombreArchivo):
        data = np.loadtxt(os.path.join('machine-learning/dataset', nombreArchivo), delimiter=',')
        # data = np.loadtxt('ex1data1.txt', delimiter=',')
        return data

    def leerExcel(nombreArchivo = 'dataset.xlsx'):
        # Leer el archivo de Excel
        data = pd.read_excel(os.path.join('machine-learning/dataset', nombreArchivo), sheet_name='Sheet1')
        # periodo = data['Periodo']
        # demanda = data['Demanda']
        # data = data.to_numpy()
        # print(data[:, 0], data[:, 1])
        return data.to_numpy()
    
    def leerExcelD(nombreArchivo = 'bank-direct-marketing-campaigns.xlsx'):
        #  str = 'edad, trabajo, marital, educación, incumplimiento, vivienda, préstamo, contacto, mes, día de la semana, campaña, días, anterior, poutcome, emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed, y'
        # Leer el archivo de Excel
        # data = pd.read_csv(os.path.join('machine-learning/datas', nombreArchivo), sheet_name='bank-direct-marketing-campaigns')
        data = pd.read_excel(os.path.join('machine-learning/dataset', nombreArchivo), sheet_name='Hoja1',)
        data = data.to_numpy()
        data = data.flatten()
        # print(data)
        # for n in data:
        #     print(n)
        # print(data[:, 0], data[:, 1])
        data =  np.genfromtxt(data, delimiter=",", dtype='str')
        return data

def NUMPY():
    # data = LeerArchivo.leerExcelD()
    # edad, trabajo, marital, educación, incumplimiento, vivienda, préstamo, contacto, mes, día de la semana, campaña, días, anterior, poutcome, emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed, y
    # data = LeerArchivo.leerTxt('dataset-victor.txt')
    data = np.loadtxt(os.path.join('machine-learning/dataset', 'dataset-victor.txt'),  dtype='str', delimiter=',')
  
    data = data[:, [0, 10, 11, 12, 14, 15, 16, 17, 18]].astype(float)

    # for i, n in enumerate(data[0]):
    #     print(i, n)
    print(data)
    # zeros = np.zeros((2,3))
    # ones = np.ones((2,3))
    # print(zeros)
    # print(ones)
    # aleatorios = np.random.random((2,4))
    # print(aleatorios)
    
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# result = np.dot(a, b)
# print(result) 
# # Output: 32


NUMPY()
