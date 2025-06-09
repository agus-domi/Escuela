temperatura=int(input("Ingrese la temperatura en °C: "))
humedad=int(input("Ingrese el porcentaje de humedad: "))
while humedad<0 or humedad>100:
    print("El porcentaje de humedad debe estar entre 0 y 100")
    humedad=int(input("Ingrese nuevamente el porcentaje de humedad: "))
viento=int(input("Ingrese la velocidad del viento: "))

frioe=False
templado=False
calor=False #Indico si hace o no frio, calor o esta templado
if temperatura<=0:
    frioe=True
elif temperatura>25:
    calor=True
elif temperatura>0 and temperatura<=25:
    templado=True
if frioe:
    print("Usar ropa abrigada y evitar exposición prolongada.")
if calor and humedad>60:
    print("Riesgo de calor húmedo, mantenerse hidratado.")
if viento>45:
    print("Mantener ventanas cerradas, evitar usar bicicleta.") #Evaluo cada variable y segun los datos damos los consejos

presionsuma=int(0)
presionmax=int(0)
for i in range(4):
    presion=int(input("Ingrese la presion: "))
    presionsuma+=presion #Sumamos cada presion ingresada para luego obtener el promedio
    if presion>presionmax:
        presionmax=presion #Evaluamos las presiones maximas
    if humedad>80 and presion<1000:
        print("¡¡Alerta de Tormenta!!")
        print(f"La presion promedio es de {presionsuma/i} hPa y la presion maxima fue de {presionmax} hPa")
        break #Verificamos si hay alerta de tormenta, si la hay se corta el ciclo
    elif i==3:
        print(f"La presion promedio es de {presionsuma/i} hPa y la presion maxima fue de {presionmax} hPa") #Si ya se ingresaron las 4 presiones muestra los datos