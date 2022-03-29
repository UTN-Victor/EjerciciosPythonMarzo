lista = [1,"hola",3.5,False]

while len(lista) > 0:
    elem = int(input("Ingrese la posicion del elemento a eliminar: "))
    print("Eliminando :",lista[elem])
    if(elem < len(lista)):
        del(lista[elem])
    else:
        print("Fuera del rango")
    
    
