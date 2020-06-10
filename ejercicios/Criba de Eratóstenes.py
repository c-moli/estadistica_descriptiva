num = int(input("Dime un número: "))
lista = list(range(2,num+1))
print(lista)

i = 0
while(i < len(lista)-1):
    for n in lista:
        if n <= lista[i]:
            # Cada iteracion del while hace que el for comience desde el primer elemento. 
            # Esto es para omitir los numeros primos ya encontrados
            continue
        elif n % lista[i] == 0:
            # Si un numero es divisible entre el elemento actual del while
            # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
            lista.remove(n)
        else:
            # Si no es divisible, entonces omitirlo (no hacer nada)
            pass
    i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)

print (lista)