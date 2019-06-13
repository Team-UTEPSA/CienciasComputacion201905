from array import *

#definiendo objeto array tipo de datos double y elementos con punto decimal
v = array('d',[45.78, 36.15, 789.253, 2.75, 55.356, 45.63, 159.789])

print('Visualizar los elementos del vector v')
print(v)
print()

print('Obtener elementos del vector')
print('v[0] = ', v[0])
print('v[1] = ', v[1])
print('v[-1] = ', v[-1])
print('v[-2] = ', v[-2])
print()

n = len(v)
print('Dimensión del vector: ', n)
print()


print('Obtener elementos del vector')
print('v[6] = ', v[6])
print('v[5] = ', v[5])
print()


#-------------------------------------------
print('Modificar el valor de los elementos del vector')
print(v)
v[3] = 999.666
print(v)
print('v[3] = ', v[3])
print()


#-------------------------------------------
print('Operacionalizar elementos del vector')
print('Sumar v[3] + v[4] = ', str(round((v[3] + v[4]), 3)))
print()


#-------------------------------------------
print('Listar los elementos del vector con for in')

for ele in v:
    print(ele)

print()


#-------------------------------------------
print('Listar los elementos del vector con while')

n = len(v)
i = 0
while i<n:
    print('v[' + str(i) + '] = ' + str(v[i]))
    i = i + 1

print()


#-------------------------------------------
print('Sumar y promediar los elementos del vector')

s = 0  #Sumatoria
p = 0  #Promedio

n = len(v)  #Dimensión del vector o número de elementos
i = 0

while i<n:
    s = s + v[i]  #Calculando la sumatoria
    i = i + 1

p = s / n  #Calculando el promedio

print('Cantidad elementos: ' + str(n))
print('Sumatoria: ' + str(round(s, 2)))
print('Promedio: ' + str(round(p, 2)))
print()


#-------------------------------------------
print('BUSCAR UN ELEMENTO EN EL VECTOR')
print()
ele = float(input('Escriba el elemento: '))

respuesta = False
posicion = -1
n = len(v)
i = 0

while i<n:
    if v[i] == ele:
        respuesta = True
        posicion = i
        i = n
    i = i + 1

if (respuesta == True):
    print('El elemento se encuentra en la posición ' + str(posicion))
else:
    print('El elemento no se encuentra en el vector')


#-------------------------------------------




    



