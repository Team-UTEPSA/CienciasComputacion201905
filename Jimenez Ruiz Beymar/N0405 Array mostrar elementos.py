import array as vec

v = vec.array('i',[5,6,8,1,2,4])

print('Elementos del vector')
print(v)

print()
print('Listar elementos con for in')

for ele in v:
    print(ele)

print()

n = len(v)
print('Dimensión del vector: ', n)
print()

print('Listar elementos con while')

i = 0
while i<n:
    print(v[i])
    i = i+1
