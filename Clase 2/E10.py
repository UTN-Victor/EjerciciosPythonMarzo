x = int(input("Ingrese el numero a evaluar: "))
i = 0
print("\nDivisores: ")
for i in range(1,(x//2)+1,i+1):
    if(x%i == 0):
        print("> ",i)
print("> ",x)