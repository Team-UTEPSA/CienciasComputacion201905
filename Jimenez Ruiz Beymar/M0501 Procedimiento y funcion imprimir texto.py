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
i = 1

ImprimirNombre(i, s)
i = Incrementar(i)

ImprimirNombre(i, s)
i = Incrementar(i)

ImprimirNombre(i, s)
i = Incrementar(i)

ImprimirNombre(i, s)
