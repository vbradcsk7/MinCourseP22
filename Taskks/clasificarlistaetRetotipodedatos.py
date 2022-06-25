'''
A partir de la tupla mostrada de distintos tipos de datos (str, int y float),
elaborar un programa para recorrerla y crear tres listas en las que se guarden
esos tipos de datos, es decir una lista para los datos de tipo int, una lista
para los datos de tipo float y una lista para los datos de tipo str, e imprimir
cada una una de las listas con sus respectivos tipos de datos por separado, así:
'''

floatci=[]
stringsb=[]
enteros=[]
Tupla = (1, 2, "Hola", 3.3, "hello", 5, 4.3)

for i in range (0,len(Tupla)):
    if(type(Tupla[i])==str):
        stringsb.append(Tupla[i])
    elif (type(Tupla[i])==int):
        enteros.append(Tupla[i])
    elif (type(Tupla[i])==float):
        floatci.append(Tupla[i])


print("Datos de tipo int\n")
print(enteros)
print("Datos de tipo float\n")
print(floatci)
print("Datos de tipo str\n")
print(stringsb)


