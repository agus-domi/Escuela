#Considerá un plano cartesiano que contiene un círculo y un punto. Determiná si el
#punto está dentro o fuera del círculo. Los datos que recibimos son:
# El origen del círculo en el plano: cX y cY
# El radio del círculo r
# El origen del punto x e y
import math
def punto(cX, cY, r, x, y):
    cat1=abs(cX-x)
    cat2=abs(cY-y)
    d=math.sqrt(cat1**2+cat2**2)
    if d>r:
        return "El punto esta afuera del circulo"
    else:
        return "El punto esta adentro del circulo"

print(punto(0, 0, 5, 2, 2))
print(punto(0, 0, 5, 3, 4))
print(punto(0, 0, 5, 6, 0))