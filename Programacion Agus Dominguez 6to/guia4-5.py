def es_primo(num):
    if num==2 or num==3:
        return "es primo"
    i=2
    while(num%i!=0):
        i+=1
    if i!=num:
        return "no es primo"
    elif i==num:
        return "es primo"
print(es_primo(4))
print(es_primo(13))