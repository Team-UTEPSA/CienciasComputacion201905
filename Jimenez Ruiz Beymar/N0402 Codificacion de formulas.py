print('CÁLCULO DE LA VELOCIDAD FINAL')
print()

vi = float(input('Escriba la velocidad inicial [km/h]: '))
a = float(input('Escriba la aceleración [km/h2]: '))
t = float(input('Escriba el tiempo [h]: '))

vf = vi + a* t**2

print()
print('La velocidad final es: ' + str(round(vf, 2)) + ' [km/h]')


#print(type(vi))
#print(type(a))
#print(type(t))
