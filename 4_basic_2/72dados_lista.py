#Extraindo dados de uma lista
lista=[]
while True:
    num=int(input('Digite um valor inteiro: '))
    lista.append(num)
    cont=str(input('Deseja continuar? [S/N] ')).strip().upper()
    while True:
        if cont not in ('S','N'):
            cont=str(input('Valor INVÁLIDO! SOMENTE "S" OU "N". Deseja continuar? [S/N] ')).strip().upper()
        else:
            break
    if cont=='N':
        break

print(f'A lista formada contém {len(lista)} elementos')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('A lista contém o número 5')
else:
    print('A lista não contém o número 5')
