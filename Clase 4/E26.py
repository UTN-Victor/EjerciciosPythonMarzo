from random import randint

def llenarAle(a,b):
    v = []
    for i in range(randint(a,b)):
        v.append([])
        for j in range(randint(a,b)):
            rand = randint(a,b)
            v[i] += [rand]
    return v

def imprimir(v):
    for i in range(len(v)):
        print("[",end="")
        for j in range(len(v[i])):
            print("%3s"%v[i][j],end="")
        print("  ]")

v = llenarAle(1,10)
imprimir(v)
