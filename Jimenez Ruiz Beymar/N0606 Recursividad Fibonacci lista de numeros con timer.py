import time

#Algoritmo RECURSIVO
def fibonacciRecursivo(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)


#Algoritmo ITERATIVO
def fibonacciIterativo(n):
    f2 = 0  #f2 = f-2
    f1 = 1  #f1 = f-1

    if n==0 or n==1:
        return n
    else:
        i = 2
        while i<=n:
            fn = f1 + f2
            f2 = f1
            f1 = fn
            i += 1
            
    return fn


#Algoritmo LINEAL rango [1..1475]
def fibonacciLineal(n):
    A = (1 + 5**(1/2))/2
    F = (A**n - (1- A)**n) / 5**(1/2)
    return round(F)

''' TOTAL 308 DÍGITOS, 77 DÍGITOS POR LINEA
49922546054780146353198579531352153533212840109029466994098142197617303359523
10426947145539056283541210440601965473058380090413298293580720257549004407513
26312032848548905058088774308376184935775127034539283793908747308299066520675
45822236147772760444400628059249610784412153766674534014113720760876471943168
'''


def listaFibonacci(cantidad):
    lstF = []
    i = 0

    while i<cantidad:
        lstF.append(fibonacciLineal(i))
        i += 1
        
    return lstF
    

#SUBPROCESO: Procedimiento Principal
def main():
    try:
        cantidad = int(input('Cuántos números de la serie Fibonacci desea generar: '))
        
        if cantidad>0:
            Tinicio = time.time()
            print(listaFibonacci(cantidad))
            Tfinal = time.time()
            Ttiempo = Tfinal - Tinicio
            print()
            print('T Inicio: ' +  str(Tinicio))
            print('T Final: ' + str(Tfinal))
            print('T Tiempo de duración [seg]: ' + str(Ttiempo))
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
