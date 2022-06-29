import math 


coeficientea=int(input("digite a:"))
coeficienteb=int(input("digite b:"))
terminoindeo=int(input("digite c:"))


rp1=((coeficienteb**2))-(4*coeficientea*terminoindeo)
if rp1<0:
    print("La ecuación no tiene soluciones reales")
else:
    raiz=math.sqrt(rp1)
    numerador=(-coeficienteb)+(raiz)
    denominador=(numerador)/(2*coeficientea)
    x1=denominador


    rp1=((coeficienteb**2))-(4*coeficientea*terminoindeo)
    raiz=math.sqrt(rp1)
    numerador1=(-coeficienteb)-(raiz)
    denominador1=(numerador1)/(2*coeficientea)
    x2=denominador1


    print(x1)
    print(x2)


