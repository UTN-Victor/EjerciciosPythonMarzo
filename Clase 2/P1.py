x = int(input("Ingrese el numero: "))

i = 0
for i in range(1,x+1,i+1):
    if(i%3==0 and i%5==0):
        print(i," FizzBuzz")
    elif(i%3==0):
        print(i," Fizz")    
    elif(i%5==0):
        print(i," Buzz")
    