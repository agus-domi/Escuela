#Considerá un plano cartesiano que contiene un círculo y un punto. Determiná si el
#punto está dentro o fuera del círculo. Los datos que recibimos son:
# El origen del círculo en el plano: cX y cY
# El radio del círculo r
# El origen del punto x e y
import math
cX=int(input("cX: "))
cY=int(input("cY: "))
r=int(input("r: "))
x=int(input("x: "))
y=int(input("y: "))
cat1=abs(cX-x)
cat2=abs(cY-y)
d=math.sqrt(cat1**2+cat2**2)
if d>r:
    print("El punto esta afuera del circulo")
else:
    print("El punto esta adentro del circulo")