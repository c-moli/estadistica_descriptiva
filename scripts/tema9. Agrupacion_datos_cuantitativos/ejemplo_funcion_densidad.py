import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

media = 10 ,20 
sd = 5,2

dist = pd.DataFrame(np.random.normal(loc = media, scale = sd, size = (1000,2)), columns = ["x1", "x2"])
dist.agg(["min", "max","mean", "std"]).round(decimals = 2)

fig, ax = plt.subplots() #se crean al figura y los ejes
dist.plot.kde(ax=ax, legend = False, title = "Histograma de dos normales")
dist.plot.hist(density = True, ax=ax)

from scipy import stats
dist = stats.norm() #distribución normal teórica
sample = dist.rvs(size = 1000) #se crea los datos en base a una distribución normal

x = np.linspace(start = stats.norm.ppf(0.01), stop = stats.norm.ppf(0.99), num = 250) #se generan los cuantiles que irían en el eje de las x. Para que empiece desde e l1% más pequeño ahsta el 99% más grande. Se generan 250 puntos en el eje de las X

gkde = stats.gaussian_kde(dataset = sample) #se calcula la distribución de la meustra. Python utilzia la gausiana
#de esta forma ya tenemos la teórica (dist) y la que tiene realmente la muestra (gkde)

fig, ax = plt.subplots()

ax.plot(x,dist.pdf(x), linestyle = "solid", c="red", lw = 3, alpha = 0.8, label = "Distribución normal teórica") #se crea la línea con la distribución teórica. En en eje x irá lso valroes creados en x. En el eje y la distribución teórica (probability density function de x)
ax.plot(x = x, gkde.evaluate(x), linestyle = "dashed", c="green", lw = 2, label = "PDF estimada por KDE")
#se crea la línea con la distribución específica de la muestra. En en eje x irá los valroes creados en x. En el eje y la distribución de la muestra utilizando la función evaluate de gkde en base a la x
ax.legend(loc = "best", frameon= False) #best l ocoloca en donde cree que es mejor
ax.set_title("Normal analítica vs estimada")
ax.set_ylabel("Probabilidad")

plt.show()