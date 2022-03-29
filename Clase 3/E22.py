from random import randint


def llenarSec(n):
    lista = []

    for i in range(1,n+1):
        lista += [i]
        
    return lista

def llenarAle(n):
    lista = []
    for i in range(1,n+1):
        num = randint(1,n)
        while num in lista:
            num = randint(1,n)
        lista += [num]
    return lista

n = 20
listaA = llenarAle(n)
print(listaA)

#Evitar repetidos, -generar parejas-
print(len(listaA)//2)
for i in range(len(listaA)//2):
    print(listaA[i]," con ",listaA[i + len(listaA)//2])
