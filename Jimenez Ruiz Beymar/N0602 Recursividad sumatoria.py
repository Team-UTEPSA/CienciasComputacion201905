def sumatoriaRec(n):
    if n==1:
        return n
    else:
        return n + sumatoriaRec(n-1)
        

#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número entero mayor que cero: '))
        if num>0:
            print('La sumatoria de ' + str(num) + ' es ' + str(sumatoriaRec(num)))
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
