import pandas as pd
import numpy as np
import math

#cargamos el data frame y lo filtramos a los datos de anchura
data = pd.read_table("C:\\Users\\cmolinero\\Documents\\GitHub\\r-basic\\data\\datacrab.txt",sep=" ")
data_w = data["width"]

#calculamos el número de clases por la regla de la raíz cuadrada

n = len(data_w)

k = math.ceil(math.sqrt(n)) #calculamos el nº de clases
print("El nº de intervalos es:",k)

A = (max(data_w)-min(data_w))/k
print(A)
A = 0.9 # A da 0.89, se redondea por arriba a la precisión.

P = 0.1 #la precisión sería la unidad más pequeña en al que se incrementan los datos. En este caso los datos tienen hasta un decimal, por lo que la precisión sería de 0.1

#Calculamos el límite inferior y el resto de intervalos
L1 = min(data_w)-1/2*P
L = L1 + A*np.array(range(k+1)) #partiendo del límite inferior se calcula el resto de límites sumando la A. Se pone el num de inetrvalos + 1; ya que se añaden los límites inferiores y superiores
print(L)

#Calculamos las marcas de clase
X1 = (L[0]+L[1])/2
X = X1 + A*np.array(range(k)) #en este caso queremos que sean el num de intervalos
print(X)

