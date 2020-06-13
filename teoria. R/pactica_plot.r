alumnos = c(1:10)
notas = c(4,5,3,6,7,4,5,8,9,5)
plot(alumnos, notas, type = "l")
plot(notas, alumnos)
plot(notas)
x=3
plot(x^(1:10),log = "y", pch = 18, main = "Función", col = "red")
plot(4,10)
funcion = function(x){
  sqrt(x)
}
plot(funcion)
plot(sqrt(9))

#Fibonacci
n= c(1:20)
par(mfrow = c(1:2)) #le digo que quiero que los gráficos estén en una distribución 1 fila y dos columnas
fib = (1/sqrt(5))*((1+sqrt(5))/2)^n - (1/sqrt(5))*((1-sqrt(5))/2)^n
plot(fib, xlab = "n", ylab = expression(F[n]), bg = "palegreen3", pch = 21)
plot(fib, type = "l", xlab = "n", ylab = expression(F[n]), bg = "blue", pch = 21)

x = c(50:59)
y = c(2,9,25,3,100,77,62,54,19,40)
plot(x,y, pch = 23, cex = 2, col = "blue", type = "p")
plot(x,y, pch = 23, cex = 2, col = "blueviolet", type = "l")
plot(x,y, pch = 23, cex = 2, col = "gold", type = "b")
plot(x,y, pch = 23, cex = 2, col = "deeppink", type = "o")
plot(x,y, pch = 23, cex = 2, col = "springgreen", type = "h")
plot(x,y, pch = 23, cex = 2, col = "firebrick1", type = "s")
par(mfrow = c(1,1))
