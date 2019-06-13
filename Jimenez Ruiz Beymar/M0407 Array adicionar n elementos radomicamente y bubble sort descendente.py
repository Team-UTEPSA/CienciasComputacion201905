from array import *
import random

v = array('i',[])

n = int(input('Escriba la cantidad de elementos del vector: '))
i = 0

while i<n:
    v.append(random.randint(0, 100))
    i = i + 1

print(v)


#Ordenar el vector en forma descendente
n = len(v)
i = 0

while i<(n-1):
    j = i + 1
    while j<n:
        if v[i]<v[j]:
            #intercambiar
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
        j = j + 1
    i = i +1

print(v)






