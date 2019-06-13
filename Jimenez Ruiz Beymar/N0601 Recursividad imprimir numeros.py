def imprimirRec(n):
    if n==0:
        print(n)
    else:
        print(n)
        imprimirRec(n-1)
        

#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número entero mayor que cero: '))
        if num>0:
            imprimirRec(num)
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
