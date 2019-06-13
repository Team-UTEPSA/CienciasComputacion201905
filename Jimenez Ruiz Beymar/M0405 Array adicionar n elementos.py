from array import *

#Definiendo el vector sin elementos
v = array('i',[])

n = int(input('Escriba la cantidad de elementos que tendrá el vector: '))
i = 0

while i<n:
    v.append(int(input('Escriba el elemento (' + str(i+1) + '/' + str(n) + '): ')))
    i = i + 1

print()
print(v)


#Modificar un elemento del vector
print(v)

pos = int(input('El elemento de qué posición desea modificar [1...' + str(len(v)) + ']: '))
valor = int(input('Qué valor tendrá esa posición: '))

pos = pos - 1
if pos>=0 and pos<n:
    v[pos] = valor

print()
print(v)


#Insertar un elemento en el vector
print(v)

pos = int(input('En que posición desea insertar un elemento [1...' + str(len(v)) + ']: '))
ele = int(input('Qué valor tendrá el elemento: '))

v.insert(pos-1, ele)

print()
print(v)



