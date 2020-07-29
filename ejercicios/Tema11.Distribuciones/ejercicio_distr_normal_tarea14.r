library(Rlab)

#Ejercicios 1. Tiempo en horas en finalizar un producto
media1 = 10
dt1 = 2

#Menos de 6 horas
pnorm(6, mean = media1, sd = dt1)

#Entre 7 y 13 horas
pnorm(13, mean = media1, sd = dt1) - pnorm(7, mean = media1, sd = dt1)

#Ejercicio 2
#El valor (en millones) de las ventas anuales realizadas en la 
#Discogr�fica "Hasta quedarnos sin t�mpanos" sigue un modelo normal 
#de media igual a 200 y desviaci�n t�pica igual a 40.

#Igual a 200 ser�a 0

#Mayor 250
1 - pnorm(250, mean = 200, sd = 40)

#Menor o igual a 100
pnorm(100, mean = 200, sd = 40)


#ejercicio 3.
#Las puntuaciones obtenidas en un examen tipo test realizado 
#a un grupo de opositores se distribuyen normalmente 
#con media 50 y desviaci�n t�pica 6.5.
media3 = 50
dt3 = 6.5

#Menos 23 puntos
pnorm(23, mean = media3, sd = dt3)

#Entre 27.3 y 43.1 puntos
pnorm(43.1, mean = media3, sd = dt3) - pnorm(27.3, mean = media3, sd = dt3)

#M�s 62 puntos
1 - pnorm(62, mean = media3, sd = dt3)

#3.2 puntos o menos
pnorm(3.2, mean = media3, sd = dt3)

#n� puntos para que la probabilidad sea de 0.045
#calculamos con la funci�n del quantil para que nos d� a partir de
#qu� valor no se supera el cuantil 0.045 (que ser�a esa probabilidad)
qnorm(0.045,  mean = media3, sd = dt3)

#n� puntos para que la probabilidad sea de 0.45
qnorm(0.45,  mean = media3, sd = dt3)
