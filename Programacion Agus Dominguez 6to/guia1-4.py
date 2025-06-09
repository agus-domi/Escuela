carreras = 0
carreras12 = 0
while (carreras<15 and carreras12<5):
    tiempo = int(input("Ingrese el tiempo del corredor: "))
    if tiempo<12:
        carreras12+=1
    carreras+=1
    if carreras==15 or carreras12==5:
        print("Sesion terminada!")