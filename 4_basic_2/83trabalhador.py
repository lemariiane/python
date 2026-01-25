from datetime import date
dicionario={}

dicionario['nome']=str(input('Nome: '))
dicionario['ano_nasc']=int(input('Ano de nascimento: '))
dicionario['num_carteira']=int(input('Número da cateira de trabalho (digite 0 caso não tenha): '))

ano_atual=date.today().year
dicionario['idade']=ano_atual-dicionario['ano_nasc']

if dicionario['num_carteira']!=0:
    dicionario['ano_contratacao']=int(input('Ano de contratação: '))
    dicionario['salario']=float(input('Salário: '))
    dicionario['aposentadoria']=dicionario['idade']+(dicionario['ano_contratacao']+35)-ano_atual

print('=-'*25)
for k,v in dicionario.items():#k= key / v=value
    print(f'O {k} é igual: {v} ')