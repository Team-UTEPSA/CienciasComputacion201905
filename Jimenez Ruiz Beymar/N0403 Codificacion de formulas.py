'''
Programador: Beymar Jiménez Ruiz
Programa: Calculo de la ley de senos
Fecha: 31/05/2019
'''

from math import sin, radians

print('CÁLCULO DE LA DISTANCIA DE UN LADO DEL TRIÁNGULO MEDIANTE LA LEY DE SENO')
print()

aAlfa = float(input('Escriba el ángulo Alfa [grados]: '))
aGama = float(input('Escriba el ángulo Gama [grados]: '))
LadoA = float(input('Escriba el tamaño del lado A [metros]: '))

LadoC = (LadoA * sin(radians(aGama)))/sin(radians(aAlfa))

print()
print('El tamaño del lado C es ' + str(round(LadoC,2)) + ' metros')



