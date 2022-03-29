def llenarSec(n):
    v = []
    k = 0
    
    for i in range(n):
        v.append([])
        for j in range(n):
            k += 1
            v[i] += [k]
    return v

def imprimir(v):
    for i in range(len(v)):
        print("[",end="")
        for j in range(len(v)):
            print("%3s"%v[i][j],end="")
        print("  ]")
        

v = llenarSec(10)
imprimir(v)
