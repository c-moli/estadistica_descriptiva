install.packages("MASS")
data = MASS::birthwt
str(data)
head(data)
help("birthwt")
tabla1 = table(
  list(
  Raza = data[,"race"],
  Peso_menos_2.5 = data[,"low"])
  )

dimnames(tabla1) = list(
  Raza = c("Blanca","Negra","Otra"),
  Peso_menos_2.5 = c("SI","NO"))

round(prop.table(tabla1),3)

plot(tabla1, col = "lightblue")
barplot(t(prop.table(tabla1)),beside = TRUE,
        ylim = c(0,0.6),xlim = c(0,9),
        col = c("orange","lightblue"))
legend(legend = c("Menos 2.5 Kg", "Más 2.5 Kg"), x = "topright", 
       fill = c("orange","lightblue"))

tabla_fumadora = table(
  list(
    Fumadora = data[,"smoke"],
    Peso_menos_2.5 = data[,"low"])
)
dimnames(tabla_fumadora) = list(
  Fuma = c("NO","SI"),
  Peso_menos_2.5 = c("SI","NO")
)

plot(tabla_fumadora, col = "lightblue")
barplot(t(prop.table(tabla_fumadora)),beside = TRUE,
        ylim = c(0,0.6),xlim = c(0,9),
        col = c("orange","lightblue"), xlab = "Madre fumadora")
legend(legend = c("Menos 2.5 Kg", "Más 2.5 Kg"), x = "topright", 
       fill = c("orange","lightblue"))

tabla_hipertensa = table(
  list(
    Peso_menos_2.5 = data[,"low"],
    Fumadora = data[,"ht"])
)
dimnames(tabla_hipertensa) = list(
  Peso_menos_2.5 = c("SI","NO"),
  Hipertensa = c("NO","SI"))

plot(tabla_hipertensa, col = "lightblue")
barplot(prop.table(tabla_hipertensa),beside = TRUE,
        ylim = c(0,0.8),xlim = c(0,9),
        col = c("orange","lightblue"), xlab = "Madre Hipertensa")
legend(legend = c("Menos 2.5 Kg", "Más 2.5 Kg"), x = "topright", 
       fill = c("orange","lightblue"))

tabla_terna = table(list(
    Raza = data[,"race"],
    Madre_Fumadora = data[,"smoke"],
    Peso_menos_2.5 = data[,"low"]))
dimnames(tabla_terna) = list(
  Raza = c("Blanca", "Negra","Otra"),
  Madre_Fumadora = c("NO", "SI"),
  Peso_menos_2.5 = c("SI","NO"))
round(prop.table(tabla_terna),3)
plot(tabla_terna, col = "lightblue")


