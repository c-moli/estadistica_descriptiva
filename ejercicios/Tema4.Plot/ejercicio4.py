import matplotlib.pyplot as plt
import numpy as np

Z = np.ones(20)
Z[-1] = 2 #para que el último quesito sea más grande

queso = np.array([0.04]*20) #creo un array indicando la separación de cada quesito
queso[-1]=0.2 # para que el último quesito esté separado más distancia

plt.pie(Z, colors=['%f' % (i/len(Z)) for i in range(len(Z))], explode=queso) #el blucle quiere decir que por cada quesito, el color va a ser igual al resultado de dividir la posición del bucle entre 20. 0 es negro y 1 es blanco. De esta forma dividimos la distancia entre 0 y 1 en 20 partes que corresponden a los 20 quesitos y cada uno coge su matiz del color (0, 0.05 etc)

plt.xticks([])
plt.yticks([])

plt.show()