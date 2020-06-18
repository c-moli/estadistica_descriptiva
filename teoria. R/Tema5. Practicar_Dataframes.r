df = iris
df$Sepal.Length
df = read.table("../data/olive.txt")
names(df)
df$X1[1:10]
str(df)
df$group.id
dim(df)
df

genero = c("Hombre","Mujer","Hombre","Mujer","Mujer","Hombre","Mujer","Hombre","Hombre","Mujer")
edad = sample(20:60,size = 10,replace = TRUE)
hijos = sample(0:3, 10,TRUE)

data_empleados = data.frame(Género = genero, Edad = edad , Hijos = hijos, stringsAsFactors = TRUE)
data_empleados
names(data_empleados)
str(data_empleados)
data_empleados[data_empleados$Género=="Mujer" | data_empleados$Edad>50,]
fix(data_empleados)
data_empleados
