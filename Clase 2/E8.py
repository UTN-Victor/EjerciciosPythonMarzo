jornada = 48
horas = 49
vhora = 2
salario = 0
pagoExtra = 3.5

if(horas <= jornada):
    print("Su salario es de $",(vhora * horas))
else:
    print("Su salario es de $",((vhora * jornada) + ((horas - jornada) * pagoExtra)))