a = float(input("a: "))
b = float(input("b: "))
x = -b/a

print("Ecuacion: %.0fx "%a + " %.0f = 0"%b)

if(a == 0 == b):
    r = "Todos los numero son solucion"
elif a == 0:
    r = "No existe solucion"
else:
    r = "La unica solucion es: %.2f"%x

print(r)