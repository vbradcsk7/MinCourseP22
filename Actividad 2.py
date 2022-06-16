import random


mylista = [1.5,1.2,1.6,2.0,5.0,6.6,9.0]


for i in range(9999999999999999999999):
    mylista.append(random.uniform(1.0,777.0))


print(mylista) 
'''
print(mylista)
posiszion=int(input("ingrese la posicion a ver: "))
print(mylista[posiszion])
'''

mylista.sort()
print("Los ordenados 0, n quedan....", mylista)


'''
Haga un programa en Python que dada una lista de 6
 elementos enteros, permita agregar 5 elementos de 
 tipo de datos real/float e imprimiros por consola. 
 imprimirlos de forma ascendente  
 '''

##Profe Solucionn 

numeros=[4.7,2.0,3.6]

n=int(input("ingresalo baby, cuantos son??"))

for i in range (n):
    nu=float(input("ingrese los addicionales pbrrr: "))
    numeros.append(nu)
    numeros.sort()

print(numeros)

