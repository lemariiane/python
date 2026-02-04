import random

def sorteando():
    valores = random.sample(range(1, 10), 5)
    print(f'Sorteando 5 valores da lista: {valores}')
    return valores

def somando(valores):
    pares=[]
    for i in valores:
        if i % 2==0:
            pares.append(i)
    print(f'A soma dos pares é {sum(pares)}')


valores=sorteando()
somando(valores)
