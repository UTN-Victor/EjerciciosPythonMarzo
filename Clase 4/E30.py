from dis import dis


def imprimir(dic):
    for indice in dic:
        print("Key: ",indice,"Value: ",dic[indice])

def agregaraEstudiante(dic,codigo,nombre):
    dic[codigo] = []
    dic[codigo].append(nombre)

    dic[codigo].append([])

def agregarNota(dic,codigo,nota):
    dic[codigo][1] += [nota]

def prom(dic):
    suma = 0
    for item in dic:
        suma += item
    return suma/len(dic)

dic= {}
imprimir(dic)
agregaraEstudiante(dic,"001","Victor")
agregarNota(dic,"001",10)
agregarNota(dic,"001",8)
agregarNota(dic,"001",7)
imprimir(dic)
print(prom(dic["001"][1]))