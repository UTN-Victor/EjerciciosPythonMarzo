a = ["hola","mundo","mamahuevo","piton"]
b = ["mundo","celular","mouse","piton"]
c = a + b
d = []
e = []
f = []

for i in a:
    if i in b:
        f += [i]
    else:
        d += [i]

for i in b:
    if i not in a:
        e += [i]

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)