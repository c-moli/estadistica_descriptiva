from scipy.stats import binom, geom, hypergeom, poisson, expon
import numpy as np

#Utilizamos una distribución de poisson

mu = 2

mean, var = poisson.stats(mu, moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)

prob_0 = poisson.pmf(0,mu)
print("La probabilidad de que haya 0 accidentes es de un %f %s"%((round(prob_0*100,2),"%")))
