'''
numero=int(input("digite su numero aquí:"))
unidad=numero%10
v1=numero//10
decena=v1%10
v2=v1//10
centena=v2%10
print("El numero "+str(numero)+" tiene "+ str(unidad)+" unidades")
print("El numero "+str(numero)+" tiene "+ str(decena)+" decenas")
print("El numero "+str(numero)+" tiene "+ str(centena)+" centenas")
'''


numero=int(input("digite su numero aquí:"))
contador=0#tamaño del numero

for i in  str(numero):
    contador+=1
print(contador)


if contador==1:
    print("unidad")
elif contador==2:
    print("decena")
elif contador==3:
    print("centena")
elif contador==4:
    print("milesima")
elif contador==5:
    print("decena de mil")
elif contador==6:
    print("centena de mil")




