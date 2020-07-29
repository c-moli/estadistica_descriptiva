from scipy.stats import binom, geom, hypergeom, poisson, expon
import numpy as np

#Utilizamos una distribucion geométrica, hasta medir el primer acierto
n = 200
p = 0.5 #es verdadero o falso, por lo que tiene una probabilidad de acertar de un 0.5

mean, var = geom.stats(p, moments = 'mv')
print("Media %f"%mean)
print("Varianza %f"%var)