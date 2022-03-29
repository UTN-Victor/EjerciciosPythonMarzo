from cgi import print_directory
from traceback import print_tb


a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))

if(a == b == c):
    print("Los 3 numeros son iguales")
elif(a == b or a == c or b == c):
    print("Hay 2 numeros iguales")
else:
    print("No hay numeros iguales")