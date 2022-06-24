#es como un excel lo guarda en tablas y son particulares
#y se identifica con separadores de punto y coma
#importar
from asyncore import read
import csv
from msilib.schema import File

'''
#forma basica para abrir y leer
#se crea un referente para la variable

with open('nombre.csv') as csvfile:
    #variable escuchante
    reader= csv.reader(csvfile,delimiter=';')
    #ciclo para  lectura
    for row  in reader:
        print(','.join(row))
'''

'''
##Otra forma de leer y abrir
result=[]

with open('nombre.csv') as File:
    reader=csv.DictReader(File)

    for row in reader:
        result.append(row)
    print(result)
'''

##Creando y escribiendo contenido en un archivo!
#una lista as tables
mydata=[["first_name","second_namee","grade"],['Alex','Brian','A'],['Paolo','Vasili','B']]

#se crea variable para definir todo el archivo
myfile=open('Ejemplo.csv','a')

#referenciando el objeto

with myfile:
    #se emplean las funciones
    writer=csv.writer(myfile)
    writer.writerows(mydata)

print("escritura completa")