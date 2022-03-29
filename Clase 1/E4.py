peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = peso/altura**2

print("Su imc es: %.2f"%imc)