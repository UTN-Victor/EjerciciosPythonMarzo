x = int(input("Ingrese el numero de dias: "))

a = x//365
m = (x%365)//30
d = ((x%365)%30)

print("Usted tiene",a,"año/s",m,"mes/es y",d,"dia/s de vida")