frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

k = 0
i = 0
for i in frase:
    if(letra == i):
        k+=1

if(k > 0):
    print("La letra " + letra + " se repitió " + str(k) + " veces")
else:
    print("No se encontraron coincidencias...")
