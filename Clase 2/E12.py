h = int(input("Ingrese la altura del triangulo: "))

i = j = 0

for i in range(h+1):
    for j in range(h-i):
        print("  ",end="")
    for j in range(2*i-1):
        print(" @",end="")
    print()