k = 150

h = [90,75,50,75,110,30,45,60]
h.sort(reverse=True)
print(h)
pMax = h[0]

i = 0
for i in range(len(h)):
    for j in range(i+1,len(h)):
        suma = h[i] + h[j]
        if suma <= 150:
            print(h[i]," con ",h[j]," = ",(h[i] + h[j]))
            if suma < pMax:
                pMax = suma
print("El peso mas grande encontrado es de: ",pMax,"kg")
