#SUBPROCESO: Función Fibonacci
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacciLista(c):
    lstF = []
    i = 0
    while i<c:
        lstF.append(fibonacci(i))
        i += 1
    return lstF


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        cantidad = int(input('Cuántos números de la serie Fibonacci desea generar: '))

        if cantidad>0:
            print(fibonacciLista(cantidad))
        else:
            print('ERROR:: Escriba un número mayor igual a cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()

