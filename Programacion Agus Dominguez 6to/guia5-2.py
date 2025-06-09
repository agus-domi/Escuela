letra='a'
palabra_secreta="ambulancia"
pista=[]
i = 0
while i < len(palabra_secreta):
    if palabra_secreta[i]==letra:
        pista.append(letra)
    else:
        pista.append('_')
    i+=1
print (f"Palabra: {''.join(pista)}")