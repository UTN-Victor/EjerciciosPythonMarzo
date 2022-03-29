from random import randint

def generarTab():
    v = []
    for i in range(3):
        v.append([])
        for j in range(3):
            v[i] += " "
    return v

def imprimir(v):
    for i in range(len(v)):
        print("[",end="")
        for j in range(len(v[i])):
            print("%3s"%v[i][j],end="")
        print("  ]")

def turnoAle():
    return randint(0,1)

def comprobarGanador(v,sim):
    win = False
    b = [0,0,0,0,0]
    for i in range(len(v)):        
        for j in range(len(v[i])):
            if(v[i].count(sim) == 3):
                win = True
            if v[j][i] == sim:
                b[i] += 1      
            if i == j and v[i][j] == sim:
                b[3] += 1
            if i == 2 - j and v[i][j] == sim:
                b[4] += 1
        
    for i in b:
        if b[i] == 3:
            win = True

    print(b)

    return win

def jugada(v,sim,turno):

    pos = pedirPos(turno)

    i = 0
    if pos > 3:
        i += 1
    if pos > 6:
        i += 1

    if v[i][(pos%3) - 1] == " " and comprobarEspacio(v) == True:
       v[i][(pos%3) - 1] = sim
    else:
        print("Turno saltado")

    return v

def pedirPos(turno):
    if turno == 1:
        pos = int(input("Posición: "))
    else:
        pos = randint(1,9)
    print("Pos: ",pos)
    return pos

def comprobarEspacio(v):
    k = 0
    hayEspacios = False
    for i in range(len(v)):
        for j in range(len(v[i])):
            if v[i][j] == " ":
                k += 1
    if k > 0:
        hayEspacios = True
    else: 
        print("0 espacios disponibles")
    return hayEspacios


v = generarTab()

imprimir(v)
sim = ""
turno = turnoAle()
print(turno)
while comprobarGanador(v,sim) == False and comprobarEspacio(v) == True:
    if turno == 1:
        sim = "x"
        print("\nTurno del jugador:")
        v = jugada(v,sim,turno)
        imprimir(v)
        turno = 0
    else:
        sim = "o"
        print("\nTurno de la IA:")
        jugada(v,sim,turno)
        imprimir(v)
        turno = 1
        
if turno == 1:
    print("\nPERDISTE.")
else:
    print("\nGANASTE :D")