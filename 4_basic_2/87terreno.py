#Calculando uma área com def
def area(l,c):
    a=l*c
    print(f'A área do terreno é {a}m2.')

print('Controle de Terrenos')
print('-'*15)
larg=float(input('Largura (m): '))
comp=float(input('Comprimento (m): '))
area(larg,comp)
