'''
##lista sencilla
lista=[]
##Listas de listas (matrices)
lista2=[["Julio",40],["Saray",15],["Julian",8]]

#primer campo fila(horiz) y segundo corchete es la columna(vert)
print(lista2[2][1])

##con for lo hace todo  i filas j columnas

for i in range(3):##3 filas es la dimension de mi matrizx
    for j in range(2): ##2 columnass
        print(lista2[i][j])
'''

'''
Realizar un programa que contenga una lista con
 10 valores enteros. Informar de cuántos de ellos son superiores a 100.
'''

from matplotlib import container


numeros=[]

canitidadnumeros=int(input("Usuario ingrese la cantidad de numeros: "))
for i in range (canitidadnumeros):
    nut=int(input("ingrese los numeros: "))
    numeros.append(nut)

limite=100
contador=0

for i in numeros:
    if i>=limite:
        contador+=1
print("Hay " +str(contador)+" numeros mayores o iguales a "+str(limite))
