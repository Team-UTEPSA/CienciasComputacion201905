from array import *
import random

v = array('i',[])

n = int(input('Escriba la cantidad de elementos del vector: '))
i = 0

while i<n:
    v.append(random.randint(0, 100))
    i = i + 1

print(v)


#Ordenar el vector en forma ascendente con el método burbuja smart

n = len(v)
i = 1
ordenado = False

while (i<n) and (ordenado==False):
    ordenado = True
    j = 0
    while j<(n-i):
        if v[j]>v[j+1]:
            ordenado = False
            aux = v[j]
            v[j] = v[j+1]
            v[j+1] = aux
        j = j + 1
    i = i + 1

print(v)

