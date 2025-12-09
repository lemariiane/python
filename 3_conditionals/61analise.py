maior_de_idade=qnt_homem=mulher_menor=0

print('-'*30)
print('CADASTRE UMA PESSOA')

while True:
    print('-'*30)

    idade=int(input('Idade: '))
    print('''[1] Feminino \n[2] Masculino \n[3] Outros \n[4] Prefiro não informar''')
    sexo=str(input('Qual o sexo? '))

    while True:
        if sexo in ('1','2','3','4'):
            break
        sexo=str(input('DADO INVÁLIDO! Qual o sexo: '))

    print('-'*30)
    continua=str(input('Deseja continuar? [S/N] ')).strip().upper()

    while True:
        if continua in ('S','N'):
            break
        continua=str(input('DADO INVÁLIDO! Digite um valor válido: [S/N] ')).strip().upper()

    if idade>=18:
        maior_de_idade+=1
    if sexo=='2':
        qnt_homem+=1
    if sexo=='1' and idade<20:
        mulher_menor+=1

    if continua=='N':
        break

print('='*20)
print(f'Total de pessoas com mais de 18 anos: {maior_de_idade}')
print(f'Tootal de homens cadastrados: {qnt_homem}')
print(f'Total de mulheres com menos de 20 anos: {mulher_menor}')
