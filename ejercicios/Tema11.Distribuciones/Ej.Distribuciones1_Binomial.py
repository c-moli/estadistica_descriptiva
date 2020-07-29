from scipy.stats import binom, geom, hypergeom, poisson, expon
import numpy as np

#Utilizamos una distribucion binomial, de n = 30 (30 individuos independientes)
n = 30
p = 0.25

dist = binom(n,p)
mean, var = dist.stats(moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)

prob_mas_25 = 1 - binom.cdf(25,n,p) #la probabilidad total menos la probabilidad acumulada de sacar 25 o menos
prob_15 = binom.pmf(15,n,p) #probabilidad específica de un valor. pmf
prob_10_menos = binom.cdf(10,n,p) #probabilidad acumulada cdf
print("La probabilidad de que 25 o más alumnos hagan deporte es de %f %s"%((round(prob_mas_25*100,2),"%")))
print("La probabilidad de que 15 alumnos hagan deporte es de %f %s"%((round(prob_15*100,2),"%")))
print("La probabilidad de que 10 o menos alumnos hagan deporte es de %f %s"%((round(prob_10_menos*100,2),"%")))
