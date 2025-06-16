temperatura=int(input("Ingrese la temperatura en °C: "))
humedad=int(input("Ingrese el porcentaje de humedad: "))
while humedad<0 or humedad>100:
    print("El porcentaje de humedad debe estar entre 0 y 100")
    humedad=int(input("Ingrese nuevamente el porcentaje de humedad: "))
viento=int(input("Ingrese la velocidad del viento: "))

frioe=False
templado=False
calor=False #Indico si hace o no frio, calor o esta templado
if temperatura<0:
    frioe=True
elif temperatura>25:
    calor=True
else: # Simplificado, ya que si no es frio ni calor, es templado en este contexto
    templado=True
if frioe:
    print("Usar ropa abrigada y evitar exposición prolongada.")
if calor and humedad>60:
    print("Riesgo de calor húmedo, mantenerse hidratado.")
if viento>45:
    print("Mantener ventanas cerradas, evitar usar bicicleta.") #Evaluo cada variable y segun los datos damos los consejos

presion=1001
presionsuma=0
presionmax=0
i=1
lista=["mañana","siesta","tarde","noche"]
while((humedad<80 or presion>1000) and i<5): 
    presion=int(input(f"Ingrese la presion de la {lista[i-1]}: "))
    presionsuma+=presion #Sumamos cada presion ingresada para luego obtener el promedio
    if presion>presionmax:
        presionmax=presion #Evaluamos las presiones maximas
    if humedad>80 and presion<1000:
        print("¡¡Alerta de Tormenta!!") 
        print(f"La presion promedio es de {presionsuma/i} hPa y la presion maxima fue de {presionmax} hPa") #Si se genera alerta de tormenta sale del bucle e imprime los datos
    elif i==4:
        print(f"La presion promedio es de {presionsuma/i} hPa y la presion maxima fue de {presionmax} hPa") #Si ya se ingresaron las 4 presiones muestra los datos
    i+=1

horasmensu=0
for i in range(4):
    hora=int(input(f"Ingrese el consumo por semana de la semana {i+1}: "))
    horasmensu+=hora #Se calculan las horas mensuales
kwhm=horasmensu*0.5 #Se calculan los kwh por mes
tamaño=float(input("Ingrese el tamaño de los paneles: "))
cantidad=int(input("Ingrese la cantidad de paneles: "))
superficie_total=tamaño*cantidad
eficiencia=int(input("Ingrese la eficiencia de los paneles: "))
while eficiencia<0 or eficiencia>100:
    print("El porcentaje de eficiencia debe estar entre 0 y 100")
    eficiencia=int(input("Ingrese nuevamente el porcentaje de eficiencia: "))
produccion = superficie_total * (eficiencia /100) * 31 #Con esta formula se calcula la energia total en kwh de los paneles
if produccion>kwhm:
    print("Se recomienda el uso de paneles solares") #Si los paneles generan mas energia de la que se gasta por mes se lo recomienda al usuario
else:
    print("No se recomienda el uso de paneles")