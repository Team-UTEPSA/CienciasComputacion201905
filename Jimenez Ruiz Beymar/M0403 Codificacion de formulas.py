'''
Convierte un monto de Dólares a Bolivianos
'''

TC_VentaD = 6.96
TC_CompraD = 6.86

MontoDolares = float(input('Escriba el monto en Dólares para cambiarlo a Bolivianos: '))

MontoBolivianos = MontoDolares * TC_CompraD

print()
print('El monto en Dólares de ' + str(MontoDolares) + ' es equivalente a '
      + str(round(MontoBolivianos,2)) + ' Bolivianos')


#print(type(Bolivianos))
#print(Bolivianos)
