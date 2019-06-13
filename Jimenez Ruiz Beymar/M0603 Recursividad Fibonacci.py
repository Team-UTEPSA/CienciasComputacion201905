#SUBPROCESO: Función Fibonacci
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número mayor igual a cero para determinar el Fibonacci: '))

        if num>=0:
            print('El Fibonacci de F(' + str(num) + ') es ' + str(fibonacci(num)))
        else:
            print('ERROR:: Escriba un número mayor igual a cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')

    
#Runner del Procedimiento Principal
main()

