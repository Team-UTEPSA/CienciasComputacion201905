def factorialRec(n):
    if n==1:
        return n
    else:
        return n * factorialRec(n-1)
        

#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número entero mayor que cero: '))
        if num>0:
            print('El factorial de ' + str(num) + ' es ' + str(factorialRec(num)))
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
