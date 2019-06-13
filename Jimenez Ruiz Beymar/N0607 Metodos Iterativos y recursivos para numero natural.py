#Listar dígitos del número de forma iteractiva
def listarDigitos(num):
    while num>0:
        dig = num%10
        print(dig)
        num = num//10


#Listar dígitos del número de forma recursiva
def listarDigitosRec(num):
    if num<10:
        print(num)
    else:
        print(num%10)
        listarDigitosRec(num//10)


#Listar dígitos del número de forma recursiva más su índice
def listarDigitosPosicionRec(num, pos):
    if num<10:
        print('num[' + str(pos) + '] --> ' + str(num))
    else:
        print('num[' + str(pos) + '] --> ' + str(num%10))
        listarDigitosPosicionRec(num//10, pos+1)


#Cuenta la cantidad de dígitos que tiene un número
def cantidadDigitos(num):
    c = 0
    
    while num>0:
        num = num//10
        c += 1
    
    return c


#Contar dígitos de forma Recursiva
def cantidadDigitosRec(num):
    if num<10:
        return 1
    else:
        return 1 + cantidadDigitosRec(num//10)



#Listar los digitos pares del número
def listarDigitosPares(num):
    while num>0:
        dig = num%10
        if dig%2==0:
            print(dig)
        num = num//10    


#Listar los digitos pares del número
def listarDigitosimpares(num):
    while num>0:
        dig = num%10
        if dig%2!=0:
            print(dig)
        num = num//10

#Sumar los dígitos de un número de forma iteractiva
def sumarDigitos(num):
    s = 0
    while num>0:
        s = s + (num%10)
        num = num//10
    return s


#Sumar los dígitos de un número de forma recursiva
def sumarDigitosRec(num):
    if num<10:
        return num
    else:
        return (num%10) + sumarDigitosRec(num//10)


#SUBPROCESO: Procedimiento Principal
def main():
    try:
        num = int(input('Escriba un número mayor que cero: '))
        
        if num>0:
            #listarDigitos(num)
            #listarDigitosRec(num)
            listarDigitosPosicionRec(num, 0)
            #print(cantidadDigitos(num))
            #listarDigitosimpares(num)
            #print(cantidadDigitosRec(num))
            #print(sumarDigitos(num))
            #print(sumarDigitosRec(num))
            
        else:
            print('ERROR:: Escriba un número mayor que cero')
    except ValueError:
        print('ERROR VALUE:: Dato invalido')


#Runner del Procedimiento Principal
main()
