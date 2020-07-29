from scipy.stats import uniform

a = 1.09
b = 2.53

loc = a
scale = b-a #en python se utiliza la escala que sería el salto que hay entre los dos puntos

dist = uniform(loc = loc, scale = scale) #guardo la distribución en el objeto dist

mean = dist.stats(moments = 'm')
print("La esperanza es de: %f"%mean)