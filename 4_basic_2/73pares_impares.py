#separando valores pares e ímpares em listas 
lista, par, impar= [], [], []
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

print(f'Os números são: {sorted(lista)}')
print(f'Os números pares são: {sorted(par)}')
print(f'Os números ímpares são: {sorted(impar)}')
