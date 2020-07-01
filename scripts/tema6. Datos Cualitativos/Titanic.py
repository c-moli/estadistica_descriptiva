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

#Tabla contingencias dos variables
tab_sex = pd.crosstab(index = titanic["survived"],columns = titanic["sex"])
tab_sex.index = ["Muere", "Sobrevive"] #cambiar nombres a las filas
print(tab_sex)

#Multidimensionales

surv_sex_class = pd.crosstab(index = titanic["survived"],
                            columns = [titanic["sex"], titanic["pclass"]],
                            margins = True)
print(surv_sex_class)
print(round(surv_sex_class/surv_sex_class.loc["All"]*100, 2)) #para poner en porcentaje redondeado