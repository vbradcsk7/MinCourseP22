'''
fichero=open('text.txt')
#Lectura o escirtura
print(fichero.read())
'''

'''
fichero=open('text.txt')
print(fichero.readline())#lee linea a linea 
print(fichero.readline())#lee linea a linea siguiente n+1
print(fichero.readline())#lee linea a linea 
print(fichero.readline())#lee linea a linea 
'''
'''
fichero=open('text.txt')#use el metodo open y abra el archivo + extension
caracter=fichero.readline(1)#variable que lee caracter per caracter[se guarda en la variable caracter]


while caracter !="":###mientras sea diferente al caracter vacio
    print(caracter)

    caracter=fichero.readline(1)# se imprime caracter por caracter
'''

'''
#Leyendo el fichero todo almacenado como una lista
fichero=open('text.txt')#use el metodo open y abra el archivo + extension
lineas=fichero.readlines()#lee todo de corrido

for i in lineas:
    print(lineas)

#w borra el contenido y crea uno nuevo
#a as .append
#x nos deeja escribir sobre el archivo cuando no exista de lo contrario tenemos une error
'''
#fichero=open('nuevo.txt','x')#use el metodo open y escriba con el metodo x
#fichero.write("Hola desde Python")#añadir info dentro del arhivo con el metodo write
#fichero.close()#siempre se abre y se cierra use close method para cerrar


##leyendo el archivo
fichero=open('nuevo.txt')#define el metodo open para abrir el archivo indicando el nombre y la extension
print(fichero.read())#en pantalla imprimir el contenido emplendo el metodo open
