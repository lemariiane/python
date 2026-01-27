dicionario={}
pessoas=[]
nome_mulheres=[]
idades=[]
media=0
while True:
    dicionario['nome']=str(input('Nome: '))
    dicionario['sexo']=str(input('Sexo: [M/F] ')).strip().upper()

    while dicionario['sexo'] not in ('M','F'):
        dicionario['sexo']=str(input('Sexo: [M/F] ')).strip().upper()

    dicionario['idade']=int(input('Idade: '))

    idades.append(dicionario['idade'])
    pessoas.append(dicionario.copy())

    cont=str(input('Deseja continuar? [S/N] ')).strip().upper()

    while cont not in ('S','N'):
        cont=str(input('ERRO! Responda apenas S ou N: ')).strip().upper()
    
    if dicionario['sexo']=='F':
        nome_mulheres.append(dicionario['nome'])

    if cont=='N':
        break

media=(sum(idades))/len(pessoas)

print('-='*30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média das idades é {media}')
print(f'As mulheres cadastradas foram {nome_mulheres}')
print('Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['idade']>=media:
        print('    ')
        for k,v in i.items():
            print(f'{k} = {v}')