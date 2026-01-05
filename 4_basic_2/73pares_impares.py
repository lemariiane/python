#separando valores pares e ímpares em listas 
lista=list()
par= list()
impar=list()
while True:
    num=int(input('Digite um número: '))
    lista.append(num)
    cont=str(input('Deseja continuar? [S/N]')).strip().upper()
    while cont not in ('S','N'):
        cont=str(input('VALOR INVÁLIDO! Digite apenas S ou N: ')).strip().upper()
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
    if cont=='N':
        break

print(f'Os números são: {lista}')
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')
