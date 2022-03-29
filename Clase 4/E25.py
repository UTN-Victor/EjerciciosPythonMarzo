def llenarPat(n,sim):
    v = []
    
    for i in range(n):
        v.append([])
        for j in range(n):
            if i == j or i + j == n - 1 or i == n//2 or j == n//2:
                v[i] += sim
            else:
                v[i] += " "
    return v

def imprimir(v):
    for i in range(len(v)):
        print("[",end="")
        for j in range(len(v)):
            print("%3s"%v[i][j],end="")
        print("  ]")
        

v = llenarPat(7,"@")
imprimir(v)
