from scipy.stats import binom, geom, hypergeom, poisson, expon
import numpy as np

#Utilizaremos una hipergeométrica

M = 70 #nº objetos totales
n = 10 #nº objetos tipo  podrido
N = 20 #nº extracciones

dist = hypergeom(M, n, N)
mean, var = dist.stats(moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)