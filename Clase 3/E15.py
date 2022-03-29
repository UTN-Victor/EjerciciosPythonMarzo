def vasos(n,x):
    total = 0
    reciclados = n//x
    sobran = n%x
    total += reciclados
    n = reciclados + sobran
    print("N: ",n,"\tReciclados: ",reciclados,"\tSobran: ",sobran,"\tTotal reciclados: ",total)
    return total

n = 30
x = 3

vasos(n,x)