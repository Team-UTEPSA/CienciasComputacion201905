#SUBPROCESO: Función Factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número mayor igual a cero para determinar el factorial: '))

        if num>=0:
            print('El factorial de ' + str(num) + ' es ' + str(factorial(num)))
        else:
            print('ERROR:: Escriba un número mayor igual a cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')

    
#Runner del Procedimiento Principal
main()

