def fatorial(num, show=False):
    """
    ->Calcula o fatorial de um número.
    num: O número a ser calculado.
    show: (opcional) Mostrar ou não a conta fatorial.
    """
    resultado=1
    while num>0:
        resultado*=num
        if show:
            print(f'{num}',end='')
            if num>1:
                print(' X ',end='')
            else:
                print(' = ',end='')
        num-=1
    return resultado
   

#help(fatorial)    
print(fatorial(4,True))
print(fatorial(6))