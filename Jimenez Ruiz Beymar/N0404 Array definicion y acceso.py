import array as vec

v = vec.array('i',[5,6,8,1,2,4])

print()
print('Elementos del vector: ', v)
print()
print('Dimensión del vector: ', len(v))
print()
print('Elemento v[0]', v[0])
print('Elemento v[1]', v[1])
print()
print('Elemento v[5]', v[5])
print('Elemento v[4]', v[4])
print()
print('Elemento v[-1]', v[-1])
print('Elemento v[-2]', v[-2])
print()
print('Sumar v[0] + v[-1]: ', str(v[0] + v[-1]))

