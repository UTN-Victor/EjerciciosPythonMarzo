from random import randint

def sel(x):
    seleccion = ""
    if(x == 1):
        seleccion = "Piedra"
    elif(x == 2):
        seleccion = "Papel"
    elif(x == 3):
        seleccion = "Tijera"
    return seleccion


win = 0
lose = 0
while(win < 3):
    player = int(input("Ingrese la opcion:\n1. Piedra\n2. Papel\n3. Tijera\n\tOpc: "))
    IA = randint(1,3)
    print("\nP:",sel(player)," vs IA:",sel(IA),"\n")
    if(player == 1 and IA == 3)or(player == 2 and IA == 1)or(player == 3 and IA == 2):
        win += 1
        print("Ganaste")
    elif(player == IA):
        print("Empate")
    else:
        lose += 1
        print("Perdiste")
    print("\n")
if(win > lose):
    print("Has ganado la partida")
else:
    print("Has perdido la partida")