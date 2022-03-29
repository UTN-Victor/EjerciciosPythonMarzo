from random import randint

v = True
while v:
    op = randint(1,2)
    n1 = randint(1,10)
    n2 = randint(1,10)
    if(op == 1):
        res = n1*n2
        print(n1," x ",n2," = ")
        rUser = int(input("Ingrese su respuesta: "))
        if(rUser == res):
            print("Correcto")
        else:
            print("Incorrecto")
            v = False
    if(op == 2):
        res = n1//n2
        print(n1," ÷ ",n2," = ",end="")
        rUser = int(input())
        if(rUser == res):
            print("Correcto")
        else:
            print("Incorrecto")
            v = False
    