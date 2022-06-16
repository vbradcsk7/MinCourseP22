'''
diccionario={"amarillo":"yellow","azul":"blue","rojo":"red","negro":"black"}

color=input("ingrese el color a traduccir: ")

print("Su traduccion es: ",diccionario[color])
'''
#Meta numeros y sume entre ellos..

numeros=[]
numeros2=[]


#n=int(input("ingresa la cantidad de datos para la listas #1: "))

for i in range (2):
    nu=int(input("ingrese los datos para la lista #1: "))
    numeros.append(nu)
print("La lista #1 queda:",numeros)


##llenando la lista 2
#n2=int(input("ingresa la cantidad de datos para la lista #2: "))

for j in range (2):
    nut=int(input("ingrese los datos para la lista #2: "))
    numeros2.append(nut)
print("La lista #2 queda:",numeros2)


##Sumando las listas

listaresultado=[]

for i in range (2):
    listaresultado.append(numeros[i]+numeros2[i])

print(listaresultado)
