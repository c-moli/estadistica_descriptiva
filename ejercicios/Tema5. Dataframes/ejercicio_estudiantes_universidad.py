import pandas as pd 
import numpy as np 
import math

data_frame = pd.read_csv("C:\\Users\\cmolinero\\Documents\\GitHub\\r-basic\\data\\run.csv")

#Pregunta 1
print("Hicieron el estudio %i estudiantes" %len(data_frame))

#Pregunta 2

hombres = len(data_frame[data_frame["genero"]=="H"])
mujeres = len(data_frame[data_frame["genero"]=="M"])
print("Hicieron el estudio",hombres, "hombres y",mujeres,"mujeres")

#Pregunta 3

def variacion_pulso(x):
    variacion = x["pulso.despues"]/x["pulso.antes"]
    return round((variacion-1)*100,2)

data_frame["variacion"]=variacion_pulso(data_frame) #añado la columna con la variacion del pulso

print("La variación media de los estudiantes según su nivel de actividad es: ")
print(round(data_frame.groupby("hace.deporte").variacion.mean(),2))

#Pregunta 4
print("La variación media del pulso entre los estudiantes que hacen deporte según su género es: ")
print(round(data_frame[data_frame["hace.deporte"]=="si"].groupby("genero").variacion.mean(),2)) #incluyo el filtro al principio

#Pregunta 5
print("La variación media del pulso entre los estudiantes que no hacen deporte deporte regularmente según si son fumadores: ")
print(round(data_frame[data_frame["hace.deporte"]=="no"].groupby("fuma").variacion.mean(),2))

#Pregunta 6
print("La variación media del pulso entre los estudiantes según su tipo de actividad es: ")
print(round(data_frame.groupby("tipo.actividad").variacion.mean(),2))