import seaborn as sns #paquete donde está el dataset
import pandas as pd
import numpy as np

titanic = sns.load_dataset("titanic")

titanic["survived"] = pd.Categorical(titanic["survived"]) #se transforma en categoría/factor
titanic["pclass"] = pd.Categorical(titanic["pclass"])
titanic["sex"] = pd.Categorical(titanic["sex"])
titanic["embarked"] = pd.Categorical(titanic["embarked"])

#Tablas de contingencias

print(pd.crosstab(index = titanic["pclass"],columns = "survived", rownames=["Clase"])) #index y columns son obligatorios. Columns le indicamos de qué columna los cuenta
print(pd.crosstab(index = titanic["survived"],columns = "count", rownames=["Supervivientes"])) #count se suele usar como comodín

#Frecuencias relativas

tab_superv = pd.crosstab(index = titanic["survived"],columns = "count") #se crea el data frame
print(round(tab_superv/tab_superv.sum(),2)) #se manipula con los métodos propios como el sum