from scipy.stats import expon

#distribución exponencial

lam = 7 #tiempo estimado de espera
dist = expon(scale = 1/lam) #guardo la distribución en el objeto dist

mean, var = dist.stats(moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)

prob_acum = expon.cdf(5,1/lam)

print("La probabilidad de esperar 5 minutos o menos es de %f"%prob_acum)