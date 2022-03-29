correctos = int(input("Ingrese el numero de aciertos: "))
errores = int(input("Ingrees el numero de errores: "))
total = correctos + errores

pcorrecto = (100/total) * correctos
perrores = (100/total) * errores

print("Su puntaje final fue: ",correctos,"/",errores)
print("Porcentajes:\nAciertos: %.2f"%pcorrecto,"\nErrores: %.2f"%perrores)