'''
Convierte un monto de Dólares a Bolivianos
'''

TC_VentaD = 6.96
TC_CompraD = 6.86

MontoBolivianos = float(input('Escriba el monto en Bolivianos para cambiar en Dólares: '))

MontoDolares = MontoBolivianos / TC_VentaD

print()
print('El monto en Bolivianos de ' + str(MontoBolivianos) + ' es equivalente a '
      + str(round(MontoDolares,2)) + ' Dólares')

#print(type(Bolivianos))
#print(Bolivianos)
