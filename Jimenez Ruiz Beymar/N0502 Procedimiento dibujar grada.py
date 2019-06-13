#MÉTODOS DEL PROGRAMADOR

def dibujarGrada(altura):
    '''PROCEDIMIENTO'''
    i = 1

    while i<=altura:
        print('# ' * i)
        i += 1

    print('=' * (altura * 2 + 5))

#FIN MÉTODOS DEL PROGRAMADOR


#MÉTODO: Función Principal
def main():
    a = int(input('Escriba la altura de la grada: '))

    dibujarGrada(a)


#Runner de la función principal
main()


