from scipy.stats import binom, geom, hypergeom, poisson, expon
import numpy as np

#Utilizamos una distribucion binomial, de n = 200 (200 preguntas independientes)
n = 200
p = 0.25 #4 opciones de respuesta, pro l oque tiene una probabilidad de acertar de un 0.25

dist = binom(n,p)
mean, var = dist.stats(moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)