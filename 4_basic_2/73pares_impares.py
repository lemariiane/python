#separando valores pares e ímpares em listas 
lista=list()
par= list()
impar=list()
while True:
    num=int(input('Digite um número: '))
    cont=str(input('Deseja continuar? [S/N]')).strip().upper()
    while cont not in ('S','N'):
        cont=str(input('VALOR INVÁLIDO! Digite apenas S ou N: ')).strip().upper()
    if cont=='N':
        break
print('cabou!')