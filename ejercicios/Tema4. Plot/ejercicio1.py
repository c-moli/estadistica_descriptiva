import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X) 
plt.plot(X, Y + 1, color='blue', alpha=1.00, linewidth = 0.5)
plt.plot(X, Y - 1, color='blue', alpha=1.00, linewidth = 0.5)
plt.xticks([]) #quitar etiquetas del eje
plt.yticks([])

plt.fill_between(X,1,Y+1,color = "blue",alpha = 0.3)
plt.fill_between(X,-1,Y-1,where = (Y-1)>=-1 ,color = "blue",alpha = 0.3) #se incluye el where para determinar qué regiones
plt.fill_between(X,-1,Y-1,where = (Y-1)<=-1 ,color = "red",alpha = 0.3)

plt.show()