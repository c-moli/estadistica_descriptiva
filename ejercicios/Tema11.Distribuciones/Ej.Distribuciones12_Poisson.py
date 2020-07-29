from scipy.stats import poisson

#se espera que ocurra el evento de cobrar cada 7 minutos. Al poner tiempo medio tengo la duda de si se usa poisson o exponencial. Si se supiera que cada 7 minutos siempre cobran entiendo que sería exponencial, pero al ser 7 minutos la media puede ser o menos o más

mu = 7 #tiempo medio espera

mean, var = poisson.stats(mu, moments = 'mv')
print("La esperanza es de: %f"%mean)
print("La varianza es de: %f"%var)

prob_5 = poisson.pmf(5,mu)
print("La probabilidad de que cobren a los 5 mins es de %f"%prob_5)

prob_5_menos = poisson.cdf(5,mu)*100
print("La probabilidad de que cobren en menos de 5 mins es de %f"%prob_5_menos)
prob_9_menos = poisson.cdf(9,mu)*100
print("La probabilidad de que cobren en menos de 9 mins es de %f"%prob_9_menos)