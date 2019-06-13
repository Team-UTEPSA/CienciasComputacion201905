#MÉTODOS DEL PROGRAMADOR

def reglaDeTres(h1, k1, k2):
    '''FUNCIÓN'''
    h2 = (h1 * k2) / k1
    return h2

#FIN MÉTODOS DEL PROGRAMADOR


#PROCEDIMIENTO: Principal
def main():
    a = 1
    b = int(input('Escriba la velocidad del vehículo [km/h]: '))
    c = int(input('Escriba la distancia a recorrer [km]: '))

    d = reglaDeTres(a, b, c)

    print('Para recorrer ' + str(c) + ' kilómetros se necesitan ' +
          str(round(d,0)) + ' horas' + ' circulando a una velocidad de ' +
          str(b) + ' km/h')


#Runner del programa principal
main()


