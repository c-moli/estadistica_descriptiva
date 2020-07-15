import numpy as np
import pandas as pd

def tabla_frec_notas(data):
    L = np.array([0,5,7,9,11])
    #cut de intervalos
    notas1 = pd.cut(data, bins = L, include_lowest=True, precision=1, right=False, labels = ["Suspendido", "Aprobado","Notable","Sobresaliente"])
    #creo primer data para unir
    df_intervalos = pd.DataFrame({"Intervalos":["[0-5)", "[5-7)","[7-9)","[9-10]"]})
    #para que haya campo común para el join
    df_intervalos["Calificación"] = pd.DataFrame(["Suspendido", "Aprobado","Notable","Sobresaliente"])
    #creo segundo data para unir
    df_notas = pd.DataFrame({"Nota":data,"Calificación":notas1})
    tabla_frec = pd.crosstab(index = df_notas['Calificación'],
           columns = "Frec. Abs")
    tabla_frec["Frec. Abs. Acum."] = tabla_frec["Frec. Abs"].cumsum()
    frec_rel = round(tabla_frec["Frec. Abs"]/tabla_frec["Frec. Abs"].sum(),2)
    tabla_frec["Frec. Rel"] = frec_rel
    tabla_frec["Frec. Rel. Acum."] = tabla_frec["Frec. Rel"].cumsum()
    tabla_final = pd.merge(left=df_intervalos,right=tabla_frec, how='left', left_on='Calificación', right_on='Calificación')
    return tabla_final

notas = np.random.randint(0,11,50)
notas2 = np.array([1,5,6,4,3,4,5,6,7,10,6,6,6,6,4,4,4,5,5,5,8,8,8,9,9,9,10,10,10])
tabla_frec = tabla_frec_notas(notas2)

print(tabla_frec)

#dos formas de acceder a la longitud
print(sum(tabla_frec["Frec. Abs"])) #suma la columna
print(tabla_frec["Frec. Abs. Acum."][3]) #se accede directamente a una posición en concreto





