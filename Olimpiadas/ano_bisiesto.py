ano = int(input("Ingrese un año: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} es un año bisiesto.")
else: 
    print(f"{ano} no es un año bisiesto.")