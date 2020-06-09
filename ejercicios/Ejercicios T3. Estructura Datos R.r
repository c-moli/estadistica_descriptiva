#Ejercicios estructura datos R

#Ejercicio 1
Harry = c(-10:27)
Harry[7]

#Ejercicio 2
vector_n = c(0:200)
ecuacion = (100*2^vector_n-7*3^vector_n)
max(ecuacion)

#Ejercicio 3
vector_n = c(0:40)
x = (3*5^vector_n-1)
x[which(x>3.5)]

#Ejercicio 4
funcion = function(num){
  real = Re(num)
  imag = Im(num)
  modulo = Mod(num)
  argumento = Arg(num)
  conjugado = Conj(num)
  vector = c(real, imag, modulo, argumento, conjugado)
  vector
}
funcion(7)

#Ejercicio 5
funcion = function(A,B,C){
  x = c((-B+sqrt(B^2-4*A*C)/2*A),
        (-B-sqrt(B^2-4*A*C)/2*A)
        )
  print(x)
}
funcion(2,7,3)

#Ejercicio 6
vec = c(0,9,98,2,6,7,5,19,88,20,16,0)
vec[v==9 | v==19 | v==20 | v==16]
vec[v>=9 & v<=20]
v2 = which(vec>=9 & vec<=20)
vec[v2]
pares = which(vec%%2==0)
pares
impar_mayor20 = which(vec%%2!=0 & vec>20)
impar_mayor20
max = which(vec == max(vec))
max
min = which(vec == min(vec))
min
v2
