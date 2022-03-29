def imprimir(dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])

dic = {}

menu = True
while menu:
    opc = int(input("Elija una opcion\n1.- Agregar producto\n2.-Facturar\n"))
    if opc == 1:
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor: ")
        dic[indice] = valor        
        print(dic)
    elif opc == 2:
        factura = True
        while factura:
            imprimir(dic)
            opf = int(input("Elija una opcion\n1.- Agregar producto\n2.-Facturar\n"))
            if opf == 1:
                total = 0
                indice = input("Ingrese el producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado...")
                else:
                    total += dic.get(indice) * cantidad
                    print("El total es: ",total)
            else:
                factura = False
                total = 0
    elif opc == 3:
        print("Saliendo.")
        menu = False
    else:
        print("Ingrese una opcion valida")