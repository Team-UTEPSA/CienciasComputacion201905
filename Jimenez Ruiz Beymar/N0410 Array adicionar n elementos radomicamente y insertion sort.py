from array import *
import time
import random


v = array('i',[])

n = int(input('Escriba la cantidad de elementos del vector: '))
i = 0

while i<n:
    v.append(random.randint(0, 1000))
    i = i + 1

#print(v)


#Ordenar el vector en forma ascendente con el método burbuja smart
Tinicio = time.time()

n = len(v)
i = 0

while i<n:
    eleins = v[i]
    j = i - 1
    while (j>=0 and v[j]>eleins):
        v[j+1] = v[j]
        j = j - 1
        
    v[j+1] = eleins
    i = i + 1

Tfinal = time.time()
Ttiempo = Tfinal - Tinicio

#print(v)
print()
print('T Inicio: ' +  str(Tinicio))
print('T Final: ' + str(Tfinal))
print('T Tiempo de duración [seg]: ' + str(Ttiempo))
