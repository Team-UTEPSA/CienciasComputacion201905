def fibonacciRec(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciRec(n-1) + fibonacciRec(n-2)
        

#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número entero mayor igual que cero: '))
        if num>=0:
            print('El Fibonacci de F[' + str(num) + '] --> ' + str(fibonacciRec(num)))
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
