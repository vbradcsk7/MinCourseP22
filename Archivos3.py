fichero=open("ciclos.txt","a")

for i in range(100):
    print(i)
    fichero.write(str(i))# convierte de entero a string
    fichero.write("\n")
fichero.close()

'''
En un grupo se toman 3 notas parciales; la primera vale el 30%, la segunda el 35%
y la tercera el 35%. Elabore un programa en python que en primer lugar calcule la 
nota definitiva de cualquier estudiante y diga si su nota es aprobatoria o no. 
En segundo lugar las notas deben ser guardadas en una archivo llamado notas.txt
'''
nota1=float(input("Digite la nota #1: "))
v1=nota1*0.3
nota2=float(input("Digite la nota #2: "))
v2=nota2*0.35
nota3=float(input("Digite la nota #3: "))
v3=nota3*0.35
resultadofinal=v1+v2+v3

fichero=open("notas.txt","a")
fichero.write(str(nota1))
fichero.write("\n")
fichero.write(str(nota2))
fichero.write("\n")
fichero.write(str(nota3))
fichero.write("\n")

if resultadofinal>=3.0:
    fichero.write("Aprobo")
    print("Aprobo")
else:
    fichero.write("Reprobo")
    print("Reprobó")

fichero.close()
