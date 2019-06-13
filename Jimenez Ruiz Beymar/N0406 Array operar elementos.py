from array import *

#Definir el vector de forma vacía
v = array('f',[])


#Mostrar elementos del vector
print(v)
print()


#Cargar n elementos al vector
print('CARGAR N ELEMENTOS AL VECTOR')
print()

n = int(input('Cuantos elementos ingresará en el vector: '))

i = 0
while i<n:
    v.append(float(input('Escriba un número con punto decimal: ')))
    i = i + 1

print()
print(v)
print()


#Ordenar el vector ascendentemente
n = len(v)
i = 0

while i<n-1:
    j = i + 1
    while j<n:
        if v[i]>v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
        j = j + 1
    i = i + 1

print(v)
print()


#Ordenar el vector descendentemente
n = len(v)
i = 0

while i<n-1:
    j = i + 1
    while j<n:
        if v[i]<v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
        j = j + 1
    i = i + 1

print(v)
print()






