'''
Realizar un programa que guarde los datos personales de usted en un 
archivo de texto llamado datos.txt. en este se escribirán los datos tales como: 
Nombre, Apellido, dirección, teléfono, celular, correo 
Por último debe mostrar toda esa información por consola
'''
datos=[]
fichero=open('datos.txt','x')#use el metodo open y escriba con el metodo x en el archivo + extension
nombre=input("Usuario escriba sus nombres: ")
datos.append(nombre)
apellido=input("Usuario escriba sus apellidos: ")
datos.append(apellido)
direcc=input("Usuario escriba su direccion: ")
datos.append(direcc)
teleff=int(input("Usuario escriba su telefono: "))
datos.append(teleff)
celul=int(input("Usuario escriba su celular: "))
datos.append(celul)
mail=input("Usuario escriba su correo: ")
datos.append(mail)

finaldata = ''.join(str(datos)) #Join: Une todos los elementos de una tupla/arreglo en 
#una cadena, utilizando un carácter hash ['' or # et al.] como separador:

fichero.write(finaldata)#añadir info dentro del arhivo con el metodo write
fichero.close()#siempre se abre y se cierra use close method para cerrar

fichero=open('datos.txt')#define el metodo open para abrir el archivo indicando el nombre y la extension
print(fichero.read())#en pantalla imprimir el contenido emplendo el metodo open


'''
# escritura en el archivo
fichero = open('new.txt', 'a')
nombre= input ("ingrese el nombre: ")
apellido= input ("ingrese el Apellido: ")
direccion= input ("ingrese la Direccion: ")
telefono= input ("ingrese el telefono: ")

fichero.write("nombre: ")
fichero.write(nombre)
fichero.write("\n")
fichero.write("Apellido: ")
fichero.write(apellido)
fichero.write("\n")
fichero.write("Direccion: ")
fichero.write(direccion)
fichero.write("\n")
fichero.write("Telefono: ")
fichero.write(telefono)
fichero.write("\n")

# cerrando el archivo
fichero.close()

# lectura de archivo
fichero = open ("new.txt")
print(fichero.read())
'''