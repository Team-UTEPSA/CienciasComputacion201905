import time


#SUBPROCESO: Función Fibonacci RECURSIVO
def fibonacciRecursivo(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)
'''
Cantidad: 35
T Inicio: 1560382714.480256
T Final: 1560382722.3243983
T Tiempo de duración [seg]: 7.844142198562622
'''


#SUBPROCESO: Función Fibonacci ITERATIVO
def fibonacciIterativo(n):
    f2 = 0
    f1 = 1

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
'''
Cantidad: 1475
T Inicio: 1560382636.244386
T Final: 1560382638.150574
T Tiempo de duración [seg]: 1.9061880111694336

Cantidad: 5000
T Inicio: 1560426632.5055277
T Final: 1560426654.7391913
T Tiempo de duración [seg]: 22.23366355895996
'''


#SUBPROCESO: Función Fibonacci ITERATIVO
def fibonacciIterativoSantalla(n):
    i, f1, f2, fn = 0, 0, 1, 0
    while i<n:
        fn = f1 + f2
        f2 = f1
        f1 = fn
        i += 1 
    return fn
'''
Cantidad: 1475
T Inicio: 1560382568.698687
T Final: 1560382570.6204727
T Tiempo de duración [seg]: 1.921785593032837

Cantidad: 5000
T Inicio: 1560426710.7062526
T Final: 1560426733.002408
T Tiempo de duración [seg]: 22.29615545272827
'''


#SUBPROCESO: Función Fibonacci LINEAL rango [1..1475]
def fibonacciLineal(n):
    A = (1 + 5**(1/2))/2
    F = (A**n - (1- A)**n) / 5**(1/2)
    return round(F)

'''
Cantidad: 1475
T Inicio: 1560382460.0548983
T Final: 1560382461.80485
T Tiempo de duración [seg]: 1.7499518394470215

TOTAL 308 DÍGITOS, 77 DÍGITOS POR LINEA
49922546054780146353198579531352153533212840109029466994098142197617303359523
10426947145539056283541210440601965473058380090413298293580720257549004407513
26312032848548905058088774308376184935775127034539283793908747308299066520675
45822236147772760444400628059249610784412153766674534014113720760876471943168
'''


#Devuelve una lista con n números de la serie Fibonacci
def fibonacciLista(c):
    lstF = []
    i = 0
    while i<c:
        #lstF.append(fibonacciRecursivo(i))
        #lstF.append(fibonacciIterativo(i))
        lstF.append(fibonacciIterativoSantalla(i))
        #lstF.append(fibonacciLineal(i))
        i += 1
    return lstF


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        cantidad = int(input('Cuántos números de la serie Fibonacci desea generar: '))

        if cantidad>0:
            Tinicio = time.time()
            
            print(fibonacciLista(cantidad))
            
            Tfinal = time.time()
            Ttiempo = Tfinal - Tinicio
            print()
            print('T Inicio: ' +  str(Tinicio))
            print('T Final: ' + str(Tfinal))
            print('T Tiempo de duración [seg]: ' + str(Ttiempo))
        else:
            print('ERROR:: Escriba un número mayor igual a cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()

