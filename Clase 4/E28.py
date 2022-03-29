dic = {}
menu = True

while menu:
    opc = int(input("Elija una opcion\n1.- Agregar\n2.-Salir\n"))
    if opc == 1:
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor:")
        dic[indice] = valor        
        print(dic)
    elif opc == 2:
        print("Saliendo.")
        menu = False
    else:
        print("Ingrese una opcion valida")