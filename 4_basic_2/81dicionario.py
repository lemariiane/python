dicionario=dict()

dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Média de {dicionario["nome"]}: '))

regra = [
    (dicionario['media'] < 5, 'Reprovado'),
    (dicionario['media'] < 7, 'Recuperação'),
    (True, 'Aprovado')]

dicionario['situacao'] = next(status for condicao, status in regra if condicao)

for c,i in dicionario.items():#c=categoria i=item
    print(f'-O {c} é igual a {i}')
