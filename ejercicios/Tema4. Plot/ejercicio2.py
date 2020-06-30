import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n) 
t = np.arctan2(y,x) #se calcula el ángulo de inclinación de cada punto con la arco tangente

plt.scatter(x,y, c = t, alpha=0.4) #se iguala el color a la t para que dependiendo de ella coja un valor
plt.xticks([])
plt.yticks([])

plt.show()