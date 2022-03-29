saldo  = 0

op = 0
while(op != 3):
    op = int(input("Ingrese la opcion:\n1. Deposito\n2. Retiro\n3. Salir\n\tOpc: "))
    if op < 0 or op > 3:
        print("Opcion no valida")
        continue
    if(op == 1):
        cant = float(input("Ingrese la cantidad: "))
        saldo += cant
    elif(op == 2):
        cant = float(input("Ingrese la cantidad: "))
        saldo -= cant
    elif(op == 3):
        print("Saliendo...")
print("Su saldo total es de $",saldo)