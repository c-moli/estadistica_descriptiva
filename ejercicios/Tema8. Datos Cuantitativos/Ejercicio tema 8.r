data = read.csv("../../data/grades.txt", header=TRUE, sep = "")

#La función moda no viene predetrmianda. Instalamos el paquete necesario
# se usa la funcion mfv (most frecuent value)
install.packages("modeest") 
library(modeest)



#Ejercicio 1
#Media, mediana y moda conjunta
round(mean(data$nota,na.rm = TRUE),2)
round(median(data$nota,na.rm = TRUE),2)
names(which(table(data$nota)==max(table(data$nota))))

#Media, mediana y moda por titulación
by(data[,2],data$estudio, FUN = mean)
by(data[,2],data$estudio, FUN = median)
by(data[,2],data$estudio, FUN = summary)
by(data$nota, data$estudio, FUN = summary)

aggregate(cbind(nota)~estudio, data = data, FUN = summary)
aggregate(cbind(nota)~estudio, data = data, FUN = mfv) #moda

medias = aggregate(nota~estudio, data = data, FUN = mean)

#Ejercicio 2
aggregate(cbind(nota)~estudio, data = data, FUN = sd)
aggregate(cbind(nota)~estudio, data = data, FUN = IQR)

#Ejercicio 3
grafico = boxplot(nota~estudio, data = data, 
        col = c("skyblue","skyblue1","skyblue2","skyblue3"),
        xlab = "Carreras", ylab = "Nota",
        main = "Boxplot de carreras universitarias")
points(medias, col = "violetred4", pch = 15) 
grafico$out
grafico$group
