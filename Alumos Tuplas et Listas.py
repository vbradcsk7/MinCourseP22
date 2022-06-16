'''
Escriba un programa con un menú de opciones para un estudiante, este podrá digitar
sus notas de un curso cualquiera, con este podrá consultar la mejor nota, la nota mas
baja y saber el promedio de notas del curso. 
'''

from traceback import print_tb


notas=[]


print("Bienvenido Alumno, elija una opción: \n"+"Insertar notas =1 \n"+"Consultar notas=2\n"+
"La peor y mejor nota=3 \n"+"Promedio final=4\n")

while (True):

    opcion=int(input("Alumno ingresa la opción: "))
    if opcion==1:
        cantidadnotas=int(input("Alumno ingresa la cantidad de notas: "))
        for i in range (cantidadnotas):
            nut=float(input("ingrese las notas: "))
            notas.append(nut)
            

    elif opcion==2:
        print("Sus calificaciones son:",notas)

    elif opcion==3:
        print("Peor nota: \n")
        print(min(notas))
        print(" Mejor nota: \n")
        print(max(notas))


    elif opcion==4:
        promedio = sum(notas)
        print(promedio/cantidadnotas)

    else:
        print("Elección incorrecta")










