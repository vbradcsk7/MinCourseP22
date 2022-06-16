from importlib.machinery import FrozenImporter
import random

import mysqlx


mylista = []

#for i in range (len(mylista)):
for i in range(8):
    mylista.append(random.randint(1,777))


print(mylista)
posision=int(input("ingrese la posicion a ver: "))
print(mylista[posision])


'''

ciudades =[]
numero_insertando=int(input("ingrese la cantidad de ciudades"))

for i in range (numero_insertando):
    ciudad=input("inggrese la ciiudad: ")
    ciudades.append(ciudad)

for i in range (numero_insertando):
    print(ciudades[i])


"los reales"....
'''
