print('='*30)
print('LOJA BARATISSÍMA')
print('='*30)
total=maior_mil=qnt_produtos=0
nome_barato=''
while True:
    nome_produto=str(input('Nome do produto: '))
    preco=float(input('Preço: '))
    continua=str(input('Deseja continuar? [S/N]')).strip().upper()

    while True:#Validação de string
        if continua in ('S','N'):
            break
        continua=str(input('VALOR INVÁLIDO! Digite um valor válido! [S/N] ')).strip().upper()

    print('-'*30)

    qnt_produtos+=1
    total+=preco

    if preco>1000:
        maior_mil+=1

    if qnt_produtos==0 or preco<mais_barato:#mais barato recebe o valor do preço no primeiro loop ou quando o preço for menor que o mais barato
        mais_barato=preco
        nome_barato=nome_produto
    
    if continua=='N':
        break

if qnt_produtos==1:
    print(f'Tívemos {qnt_produtos} produto cadastrado.')
else:
    print(f'Foram {qnt_produtos} produtos cadastrados.')

print(f'O total da compra foi: R${total}')
print(f'Temos {maior_mil} produtos com o valor maior de R$1.000')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato}')
