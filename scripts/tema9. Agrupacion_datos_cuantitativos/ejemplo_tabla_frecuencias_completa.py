import numpy as np
import pandas as pd

#datos de notas
notas = np.random.randint(0,11,50)

#definimos los extremos de los intervalos
L = np.array([0,5,7,9,10.01])

#cut 1, las notas codificados según el intervalo
notas1 = pd.cut(notas, bins = L, include_lowest=True, precision=1, right=False)

#cut 2, las notas codificados según las marcas de clase (MC)
MC = (L[0:4]+L[1:5])/2
notas2 = pd.cut(notas, bins = L, include_lowest=True, right=False, labels = MC)

#cut 3, las notas codificados según etiquetas
notas3 = pd.cut(notas, bins = L, include_lowest=True, precision=1, right=False, labels = ["Suspendido", "Aprobado","Notable","Sobresaliente"])

#Tabla frecuencias Absolutas y Relativas
df = pd.DataFrame({"Nota":notas,"Intervalo":notas1,"Calificación":notas3})
intervalos = pd.DataFrame({"Intervalos":["[0-5)", "[5-7)","[7-9)","[9-10]"]})
calificaciones = pd.DataFrame({"Intervalos":["Suspendido", "Aprobado","Notable","Sobresaliente"]})
#creo una columna para que luego al hacer el join haya una común. Hago que coincida en Calificación
intervalos["Calificación"] = calificaciones


tabla_frec = pd.crosstab(index = df['Calificación'],
           columns = "Frec. Abs")

#se añade la absoluta acumulada
tabla_frec["Frec. Abs. Acum."] = tabla_frec["Frec. Abs"].cumsum()
#se calcula la frec. relativa
frec_rel = round(tabla_frec["Frec. Abs"]/tabla_frec["Frec. Abs"].sum(),2)
#se añade la relativa y la relativa acumulada
tabla_frec["Frec. Rel"] = frec_rel
tabla_frec["Frec. Rel. Acum."] = tabla_frec["Frec. Rel"].cumsum()

#es como hacer un left join de SQL. Así he podido juntar el dataFreme de la tabla de frecuencias co nel dataframe de
tabla_final = pd.merge(left=intervalos,right=tabla_frec, how='left', left_on='Calificación', right_on='Calificación')
print(tabla_final)

import matplotlib.pyplot as plt

histograma = plt.hist(x = notas, bins=L, color = "#0505a5", alpha = 0.75, rwidth=0.85)
plt.xlabel("Notas") #etiqueta de x
plt.ylabel ("Frecuencia") #etiqueta de y
plt.xticks(range(11)) #para poner todos los nº en el eje x. De manera predeterminada salta de dos en dos. Range(11) paar que ponga del 0 al 10. Se podrái haber pasado uan lista también [0,1,2,3,4,5,6,7,8,9,10]
plt.title("Histograma de frecuencias de notas") #título
plt.show()




