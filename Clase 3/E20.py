lista = [2,2,2,3,4,4,4,4,1,1,1,1,1,1]
print(lista)
i = 0
for i in range(len(lista)-1,-1,i-1):
    if lista[i] in lista[0:i]:        
        del(lista[i])
        print(lista)
