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

plt.figure(1)
plt.subplot(2,1,1)
plt.plot([1,3,5,7])
plt.subplot(2,1,2) #sin esta instrucción se harían las dos rectas en la misma gráfica
plt.plot([7,5,3,1])
plt.show()