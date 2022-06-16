'''
Desarrolle un programa en Python que almacenen   en una lista los 
días laborales de la semana, también que permita almacenar las horas
que se trabaja en cada día laboral, el programa debe imprimir los días
laborales juntos con la cantidad de horas trabajadas. 
'''
Diasdesemana= ('Lunes', 'Martes', 'Miercoles','Jueves','Viernes','Sábado','Domingo')
horasparatododiatrabajado=[]

for i in range (len(Diasdesemana)):
    numhoras=int(input("ingrese las horas trabajadas: "{Diasdesemana[x]}))
    horasparatododiatrabajado.append(numhoras)

for i in range (len(Diasdesemana)):
    print("El dia {Diasdesemana[x]},son")
print("Dias laborados y horas:",horasparatododiatrabajado)


'''
dias= ("lunes", "martes", "miercoles", "Jueves","viernes")
horas = []

for x in range (len(dias)):
hora =input(f"Ingrese la hora para el dia {dias[x]} :")
horas.append(hora)

for x in range(len(dias)):
print(f" El dia {dias[x]}, son : {horas[x]}")

print("Fin del programa"
'''