#SUBPROCESO: Función Sumatoria
def sumatoriaRec(n):
    if n==1:
        return n
    else:
        return n + sumatoriaRec(n-1)


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número mayor igual a cero para determinar la sumatoria: '))

        if num>=0:
            print('La sumatoria de los ' + str(num) + ' primeros números es ' + str(sumatoriaRec(num)))
        else:
            print('ERROR:: Escriba un número mayor igual a cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')

    
#Runner del Procedimiento Principal
main()

