#Lista los dígitos de un número natural de forma ITERATIVA
def listarDigitos(num):
    while num>0:
        dig = num%10  #Leyendo el dígito
        print(dig)
        num = num//10  #Eliminado el último dígito


#Lista los dígitos de un número natural de forma RECURSIVA
def listarDigitosRec(num):
    if num<10:
        print(num)
    else:
        print(num%10)
        listarDigitosRec(num//10)


#Lista los dígitos de un número natural de forma ITERATIVA
def listarDigitosPosicion(num):
    pos = 0
    while num>0:
        print('num[' + str(pos) + '] -->' + str(num%10))  #Leyendo el dígito
        num = num//10  #Eliminado el último dígito
        pos += 1


#Lista los dígitos de un número natural de forma RECURSIVA
def listarDigitosPosicionRec(num, pos):
    if num<10:
        print('num[' + str(pos) + '] -->' + str(num))
    else:
        print('num[' + str(pos) + '] -->' + str(num%10))
        listarDigitosPosicionRec(num//10, pos+1) 
        

#cuenta los dígitos de un número de forma ITERATIVA
def contarDigitos(num):
    c = 0
    while num>0:
        c += 1
        num = num//10
    return c


#cuenta los dígitos de un número de forma RECURSIVA
def contarDigitosRec(num):
    if num<10:
        return 1
    else:
        return contarDigitosRec(num//10) + 1


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número mayor que cero: '))
        
        if num>0:
            #listarDigitos(num)
            #listarDigitosRec(num)
            #listarDigitosPosicion(num)
            #listarDigitosPosicionRec(num, 0)
            #print(contarDigitos(num))
            print(contarDigitosRec(num))
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
