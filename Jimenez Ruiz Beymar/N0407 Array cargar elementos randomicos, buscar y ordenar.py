from array import *
import random

v = array('i',[])


#Cargar elementos en el vector randomicamente
n = int(input('Escriba el número de elementos del vector: '))

i = 0

while i<n:
    v.append(random.randint(0, 100))
    i = i + 1

print(len(v))
print(v)
print()


#Buscar un elemento en el vector
ele = int(input('Escriba el elemento que desea buscar: '))

n = len(v)
c = 0
i = 0

while i<n:
    if v[i] == ele:
        c = c + 1
    i = i + 1

if c > 0:
    print('El elemento ' + str(ele) + ' está en el vector y se repite ' + str(c) + ' veces')
else:
    print('El elemento ' + str(ele) + ' no está en el vector')








