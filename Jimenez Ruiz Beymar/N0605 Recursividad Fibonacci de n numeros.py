def fibonacciRec(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        cantidad = int(input('Cuántos números de la serie Fibonacci desea generar: '))
        
        if cantidad>0:
            i = 0
            while i<cantidad:
                print('F(' + str(i) + ') --> ' + str(fibonacciRec(i)))
                i += 1
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
