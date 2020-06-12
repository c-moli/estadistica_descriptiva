import math

#Ejercicio 1

def ecuacion(a,b,c):
    x_1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x_2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print(x_1,x_2)

#Ejercicio 2

def palindromo():
    frase = input("Dime una frase: ").replace(" ","").lower()
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

palindromo()

#Ejercicio 3
diccionario = {}
for i in range(1,11):
    diccionario[i]=math.sqrt(i)
print(diccionario)

#Ejercicio 4
codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..","0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}

frase = input("Dime una frase: ")
frase_morse=""

for letra in frase:
    letra1=letra.lower()
    frase_morse = frase_morse + " " + codigo_morse[letra1]

print(frase_morse)

#Ejercicio 5

alumno1 = {"nombre":"Carlos", "edad":30, "ciudad":"Madrid"}
alumno2 = {"nombre":"María", "nota_media":7, "asignatura":"Matemáticas"}

def claves_dic(dicc1,dicc2):
    claves1=list(dicc1.keys())
    claves2=list(dicc2.keys())
    coincide = []
    for i in claves1:
        if i in claves2:
            coincide.append(i)
    print("Coinciden las claves: ", coincide)

claves_dic(alumno1,alumno2)

#Ejercicio 6
def es_primo(num):
    es_primo = True
    for i in range(2,num):
        if num%i==0:
            es_primo=False
    if es_primo == True:
        print("El número es primo")
    else:
        print("El número no es primo")
    
es_primo(22)

#Ejercicio 7
frase = input("Dime una frase: ")
palabras = frase.split(" ")
for palabra in palabras:
    print(palabra[0].upper())

#Ejercicio 8

def MCD(a,b):
	if b ==0:
		return a
	else:
		if a>b:
			a=a-b
			b=b
			return MCD(a,b)
		else:
			c=b-a
			a=b
			b=c
			return MCD(a,b)

print(MCD(33,22))

#Ejercicio 10

lista_nombres = ["Carlos", "Ana", "Pedro", "Marcos", "Petra", "Francisco"]
print(sorted(lista_nombres))
print(sorted(lista_nombres,reverse=True))
print(sorted(lista_nombres,key=lambda nombre: len(nombre)))
print(sorted(lista_nombres,key=lambda nombre: len(nombre),reverse=True))