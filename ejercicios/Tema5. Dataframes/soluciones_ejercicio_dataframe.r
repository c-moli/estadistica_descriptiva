df_medals = read.csv("http://winterolympicsmedals.com/medals.csv")

#Pregunta 1

nrow(df_medals)

#Pregunta 2
total_medallas <- aggregate(df_medals$Medal, list(Medalla = df_medals$Medal), length)
total_medallas



#Pregunta 3
lista_ciudades <- unique(df_medals$City)
lista_ciudades
length(lista_ciudades)

#Pregunta 4
total_genero <- aggregate(df_medals$Event.gender, list(Genero = df_medals$Event.gender), length)
total_genero

#Pregunta 5
sort(table(df_medals$Year), dec = TRUE)

#Pregunta 6
df_Pais <- subset(df_medals,
                  df_medals$Medal == "Gold" & df_medals$Year>=1960 
                  & df_medals$Year <= 1996 ,
                  select = c("Year","NOC"))
row.names(df_Pais)=1:nrow(df_Pais)
sort(table(df_Pais$NOC), dec = TRUE)
