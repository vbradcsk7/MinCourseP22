'''
Escriba un programa con un menú de opciones para un estudiante, este podrá digitar
sus notas de un curso cualquiera, con este podrá consultar la mejor nota, la nota mas
baja y saber el promedio de notas del curso. 
'''

from traceback import print_tb


notas=[]


print("|Bienvenido Alumno, elija una opción: \n"+"|Insertar notas =1 |\n"+"|Consultar notas=2|\n"+
"|La peor y mejor nota=3| \n"+"|Promedio final=4|\n")

while (True):

    opcion=int(input("Alumno ingresa la opción: "))
    if opcion==1:
        cantidadnotas=int(input("Alumno ingresa la cantidad de notas: "))
        notas.clear()##borar todo el arreglo cuando el usuario elija la opcion
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


##Otra solucion:::
'''

"""
caso notas del estudiante


notas = []
print("--PROGRAMA PARA CALCULAR NOTA DE UN ESTUDIANTE--")
menu= """
1. ingresar nota
2. mejor nota
3. peor nota
4. promedio
5. mostrar las notas
6. salir
"""
print(menu)
opcion = int (input ("ingrese una opcion: "))
calificacion = 0
while (opcion != 6):
if opcion ==1 :
calificacion =float(input("Ingrese la nota: "))
notas.append(calificacion)
elif opcion==2:
mejornota= 0
for nota in notas:
if nota>mejornota:
mejornota = nota
print("la mejor notas es:", mejornota )
elif opcion==3:
peornota= 5
for nota in notas:
if nota<peornota:
peornota = nota
print("la peor notas es:", peornota )

 elif opcion== 4:
acumulador= 0
for nota in notas:
acumulador= acumulador + nota
#promedio = acumulador/
print("promedio de notas es:",acumulador/len(notas))
elif opcion== 5:
print("Sus notas son:",notas)
else:
print(" opcion incorrecta")

 print(menu)
opcion = int (input ("ingrese una opcion: "))
'''







