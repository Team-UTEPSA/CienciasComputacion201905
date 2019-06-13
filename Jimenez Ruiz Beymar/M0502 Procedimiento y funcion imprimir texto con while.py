# MÉTODOS DEL PROGRAMADOR

def Incrementar(n):
    '''Función: Incrementar'''
    n += 1
    return n


def ImprimirNombre(k, t):
    '''Procedimiento: ImprimirNombre'''
    print(str(k) + '. ' + t)

# FIN MÉTODOS DEL PROGRAMADOR


s = 'Profe Mario Justiniano'
n = int(input('Cuántas veces desea escribir el texto: '))
print()

i = 1
while i<=n:
    ImprimirNombre(i, s)
    i = Incrementar(i)
