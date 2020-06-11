import numpy as np 

lista1 = [1,2,3,4,5,6,7,8]

x1 = np.array(lista1)
x2 = np.zeros((3,4), dtype= 'int_')
x3 = np.ones((4,3), 'float_')
x4 = np.arange(2,21,2) # num inicial, num final y de cuanto en cuanto
x5 = np.linspace(1,10,5) # x numeros equidistantes entre un num y otro
x6 = np.eye(6) #forma la diagonal con el tamaño de fials y columnas que el indicamos
x6.reshape((12,3)) #se cambia la forma
x3.flatten() #aplana los datos en una sola fila

#Ejercicios
print(np.arange(5,120))
lista2 = list(range(16))
print(np.array(lista2).reshape((4,4)))
print(np.eye(7))
print(np.arange(20).reshape((5,4)))
print(np.linspace(0,5,20))

print(x6.size,
      x6.shape,
      x6.ndim)
