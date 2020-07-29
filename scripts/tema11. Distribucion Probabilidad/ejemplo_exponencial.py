from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt

#el tiempo esperado de espera, por ejemplo para que entre una llamada, es de 5 mins. lambda = 5
lam = 5 #en python se utiliza la escala de la lambda. 1/lambda

prob_especi = expon.pdf(2,1/lam) #calcularía la probabilidad de esperar justo 2 minutos para recibir una llamada
prob_acum = expon.cdf(5,1/lam) #calcularía el acumulado de las probabilidades hasta llegar a 5 minutos. probabilidad de recibir la llamada en un minuto + probailidad de recibirla en dos minutos...así hasta 5. Como el tiempo esperado (lambda) era 5 tenderá a ser 1; es decir el 100% deprobabilidad de recibir una llamada en 5 mins o menos
print("La probabilidad de recibir una llamada en justo dos minutos es de",round(prob_especi,4)*100,"%")
print("La probabilidad de recibir una llamada en 5 minutos o menos es de", round(prob_acum,4)*100,"%")

#para calcular la probalidad del evento esperando varios minutos: 

#creamos un array de numpy de 0 a 10 segundos (se pone 11 porque puython quita uno del final)
x = np.arange(0,11)

# le pasamos a la función la x con los diferentes segundos y el tiempo esperado. Nso devolverá un objeto numpy en formato array con 10 valores; que serán las probalidades para que ocurra el evento esperando x minutos. La primera posición esperando 0 minutos, la segunda esperando 1 minuto etc
prob_especi2 = expon.pdf(x,1/lam)
prob_acum2 = expon.cdf(x,1/lam)
print(np.round(prob_especi2,3)) #se utiliza el método round de numpy al ser un objeto numpy
print(np.round(prob_acum2,2))

fig, ax = plt.subplots(1,1)
ax.vlines(x,0,prob_acum2,colors = 'b', lw = 4, alpha = 0.5)

plt.show()