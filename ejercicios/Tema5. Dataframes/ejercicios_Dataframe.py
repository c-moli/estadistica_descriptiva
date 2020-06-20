import pandas as pd 
import numpy as np

df = pd.read_csv("http://winterolympicsmedals.com/medals.csv")

#Ejercicio 1
"""deportistas = df.Year.count()
print("En el evento hubo %i deportistas" %deportistas)"""

#Ejercicio 2

"""oro = df[df["Medal"]=="Gold"].Year.count()
plata = df[df["Medal"]=="Silver"].Year.count()
bronce = df[df["Medal"]=="Bronze"].Year.count()
print("Se ganaron",oro, "medallas de oro,", plata, "de plata y", bronce, "de bronce")"""

#Ejercicio 3

"""ciudades = set(list(df["City"])) #convierto a una lista las ciudades y con set cojo los valores únicos
print("Ha habido %i ciudades diferentes" %len(ciudades))"""

#Ejercicio 4

"""hombres = df[df["Event gender"]=="M"]
mujeres = df[df["Event gender"]=="W"]
print("Compitieron", len(hombres), "hombres y ", len(mujeres), "mujeres")"""

#Ejercicio 5

agnos = list(df["Year"])

def contar_elementos(lista):
    return {i:lista.count(i) for i in lista}

resultado = contar_elementos(agnos)
maximo=max(resultado, key=resultado.get)
print("El año con más deportistas es el",maximo, "con", resultado[maximo],"deportistas")