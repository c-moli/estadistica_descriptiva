df = read.csv("http://winterolympicsmedals.com/medals.csv")

#Pregunta 1
num_deportistas = nrow(df)
print(paste("El nº de deportistas es:", num_deportistas))

#Pregunta 2
medallas = aggregate(Medal~df$Medal, df, FUN = length)
colnames(medallas) = c("Metal","Numero")
medallas
print(paste("Hay",medallas[2,2], "medallas de oro,",medallas[3,2], 
            "de plata y",medallas[1,2],"de bronce."))

#Pregunta 3
lugares = as.factor(select(df,starts_with("City")))
class(lugares)
levels(lugares)
lista_ciudades = unique(df$City)
length(lista_ciudades)

#Pregunta 4
genero = aggregate(Event.gender~df$Event.gender, df, FUN = length)
genero
print(paste("Hay ", genero[1,2], "hombres y ", genero[2,2], "mujeres"))

#Pregunta 5
agnos = aggregate(Discipline~df$Year, df, FUN = length)
max_agno = subset(agnos, Discipline == max(agnos[,2]),select = 1)
print(paste("El año con más participantes fue el",max_agno))

#Pregunta 6
str(df)
ganadores = aggregate(Medal~df$NOC+df$Year, df, FUN = length)
ganadores
ganadores_1960_1996 = subset(ganadores, ganadores$`df$Year`>=1960 & 
                               ganadores$`df$Year`<=1996)
ganadores_paises = aggregate(ganadores_1960_1996$Medal~ganadores_1960_1996$`df$NOC`,
                     ganadores_1960_1996,FUN = sum)
ganadores_paises
max(ganadores_paises[,2])
max_pais = subset(ganadores_paises, ganadores_paises$`ganadores_1960_1996$Medal`
                  == max(ganadores_paises[,2]))
colnames(max_pais) = "País"
max_pais
