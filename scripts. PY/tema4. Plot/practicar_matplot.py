import matplotlib.pyplot as plt 
import numpy as np

y = [6,2,4,9]
x = [1,2,3,4]
plt.plot(x,y,"ro") #se combian el color con el estilo. r:red y o:círculos
plt.xlabel("Eje abcisas")
plt.ylabel("Eje ordenadas")
plt.axis([0,10,0,10]) # 4 números. Lso dos primeros para eje x; otros dos eje y

data = np.arange(0.0, 10.0, 0.2)
plt.plot(data,data,"b--")

plt.show()