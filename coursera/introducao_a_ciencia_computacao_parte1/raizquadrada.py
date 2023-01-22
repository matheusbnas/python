import math

a= float(input("digite o valor de A:", ))
b= float(input("digite o valor de B:", ))
c= float(input("digite o valor de C:", ))

delta= b**2 - 4*a*c

if delta == 0:
   raiz1= (-b + math.sqrt(delta))/(2 * a)
   print("tem somente uma raiz :", raiz1 )
else:
    if delta < 0:
      print("não tem raízes reais" )
    else:
     raiz1= (-b + math.sqrt(delta))/(2 * a)
     raiz2= (-b - math.sqrt(delta))/(2 * a)
     print("o valor de x1 é :", raiz1)
     print("o valor de x2 é :", raiz2)