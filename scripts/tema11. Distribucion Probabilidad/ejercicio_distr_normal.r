library(Rlab)

#500 alumnos, media del peso 75 y desviación típica 4

mu = 75
sigma = 4

#1 calcular probabilidad entre 65 y 80 kilos.
#Por definición de las tablas es igual a la probabilidad de <=80 menos la de <=65
pnorm(80, mean = mu, sd = sigma)-pnorm(65, mean = mu, sd = sigma)

# calcular prob. más de 90 kilos. Será igual a 1 menos la probabilidad de <=90
1 - pnorm(90, mean = mu, sd = sigma)

#calcular prob. 69 kilos. En variables continuas, al ser "infinitas" y estar todas muy cerca de cero se considera como 0. es un suceso con probabilidad 0 pero no imposible

#Menos de 70 kilos
pnorm(70, mean = mu, sd = sigma)

#69 kilos o más. Será igual a restar a 1 la probabilidad de <=69
1 - pnorm(69, mean = mu, sd = sigma)

menos70 = pnorm(70, mean = mu, sd = sigma)
mas70 = 1 - pnorm(70, mean = mu, sd = sigma)
menos70 + mas70
