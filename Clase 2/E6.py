sexo = "m"
edad = int(input("Ingrese su edad:"))
aServ = 26
cot = 751
apl = ""

if (aServ < 25 and cot < 750) and ((sexo == "h" and edad < 60) or (sexo == "m" and edad < 55)):
    apl = "no"
print("Usted " + apl + "aplica para ser jubilado.")