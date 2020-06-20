import pandas as pd 

df = pd.read_csv("C:\\Users\\cmolinero\\Documents\\GitHub\\r-basic\\data\\bodyfat.txt",delimiter=" ", decimal=".")
df.head(8) #imprimir las primeras filas que queramos
df.tail(5) #imprimir las últimas filas que queramos

df.loc[[1]] #acceder a la fila que queremos por identificador. Empiezan desde 1
df.iloc[[0]] #acceder a la fila que queremos por posición. Empiezan desde 0 como siempre en python
df[10:15] #acceder desde la 10 a la 14 (python excluye siempre al último)
df[0:20:2] #el 3er parámetro indica si queremos salto
df.Density.describe() #para acceder a las columnas se hace con el .
descripcion = df.describe()
descripcion.transpose() #cambiar filas y columnas
df.shape #tamaño
df.count()[0] #hace la función count a todas las columnas y la filtramos al primer elemento de la lista que devuelve


