def bisiesto(a,b):
    i = 0
    for i in range(a,b+1,i+1):
        if((i%400 == 0 or i%100 != 0) and (i%4 == 0)):
            print("> ",i)
    return 0


a = int(input("Ingrese el año menor: "))
b = int(input("Ingrese el año mayor: "))

if(a > b):
    aux = b
    b = a
    a = aux

bisiesto(a,b)
