#lista com valores únicos
lista=[]

while True:
    try:
        num=int(input('Digite um valor: '))
        if num not in lista:
            print('Valor adicionado com sucesso...')
            lista.append(num)
        else:
            print('Valor REPETIDO! Não vou adicionar...')
            
    except ValueError:
        print('Erro: Por favor, digite apenas números inteiros.')
        continue

    continua=str(input('Quer continuar? [S/N]')).strip().upper()

    while continua not in ('S','N'):
        continua=str(input('Valor INVÁLIDO! Digite [S/N]: ')).strip().upper()

    if continua in 'N':
        break

print('-'*30)
print(sorted(lista))
