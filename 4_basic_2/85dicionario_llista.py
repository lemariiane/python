pessoas=[]
while True:
    dicionario={}
    dicionario['nome']=str(input('Nome: '))
    dicionario['sexo']=str(input('Sexo: [M/F] ')).strip().upper()

    while dicionario['sexo'] not in ('M','F'):
        dicionario['sexo']=str(input('Sexo: [M/F] ')).strip().upper()

    dicionario['idade']=int(input('Idade: '))

    pessoas.append(dicionario.copy())

    cont=str(input('Deseja continuar? [S/N] ')).strip().upper()

    while cont not in ('S','N'):
        cont=str(input('ERRO! Responda apenas S ou N: ')).strip().upper()

    if cont=='N':
        break
print('-='*30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média das idades é {media}')
print(f'As mulheres cadastradas foram {nome_mulheres}')
print('Lista das pessoas que estão acima da média:')
print(f'{pessoas_acima_media}')
