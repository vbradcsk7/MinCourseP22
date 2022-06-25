'''
#escirbir una lista con el cuadrado del 1 al 1200 y print bbe
listacuadradods=[]


for i in range(1,1201):
    cuadros=i**2
    listacuadradods.append(cuadros)
print(listacuadradods)


#lista al cubo del 1 al 1000 e imprima

listacybos=[]

for i in range(1,1001):
    cubo=i**3
    listacybos.append(cubo)
tupla_cubs=tuple(listacybos)
print(tupla_cubs)
'''

#escriba las letras del abecedario  sin ll ni ñ o Ch con ACII todo en una tupla.
#en minucukla
lista_abc=[]
for i in range(97,123):#del 91 al 123 en acci al minuscu
    lista_abc.append(chr(i))#chr function es
tupla_abc=tuple(lista_abc)
print(tupla_abc)
#help(chr) recorta la cadena unicode dado el codigo en ACII

#Mayuscula

lista_abcmay=[]
for i in range(65,91):# de 65 a 91 va el accii en mayusculas
    lista_abcmay.append(chr(i))#chr function es
tupla_abcmay=tuple(lista_abcmay)
print(tupla_abcmay)


#en minucukla et condicion
lista_abc1=[]
for i in range(97,123):#del  vea tabla 91 al 123 en acci al minuscu
    if chr(i) !="b":
        lista_abc1.append(chr(i))#chr function es
tupla_ab1c=tuple(lista_abc1)
print(tupla_ab1c)



listaplabra=[]

for ii in range (0,len(tupla_abc)):
    if ii==7:
        listaplabra.append(tupla_abc[ii])
    elif ii==14:
        listaplabra.append(tupla_abc[ii])
    elif ii==11:
        listaplabra.append(tupla_abc[ii])
    elif ii==0:
        listaplabra.append(tupla_abc[ii])
    
print(listaplabra)
    


print(listaplabra)