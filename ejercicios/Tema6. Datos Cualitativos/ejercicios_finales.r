#Ejercicio 1
alumnos = c("Carlos", "María", "Pepe", "Manuel", "María", "Marta", "Ana",
            "Pepe", "Ana María")
tabla_alumnos = table(alumnos)
tabla_alumnos

#Ejercicio 2

edades = sample(18:30,20,replace = TRUE)
prop.table(table(edades))

#Ejercicio 3
altura = round(runif(n = 10, min = 1.65, max = 2.00),2)
peso = sample(60:90, 10, replace = T)
tabla_altura_peso = table(altura, peso)

#Ejercicio 4

prop.table(tabla_altura_peso)

#Ejercicio 5

barplot(table(edades), col = "lightblue", main = "Edades",
        ylim = c(0,5))

#Ejercicio 6

pie(table(alumnos), sub = "Frecuencias nombres")

#Ejercicio 7

tabla = DNase["density"]
barplot(table(tabla),col = "red",main = "Frecuencias Densidad")

        