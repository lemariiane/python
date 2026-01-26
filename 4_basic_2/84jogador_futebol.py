dicionario={}
gols=[]
partida_gol={}
dicionario['nome']=str(input('Nome jogador: '))
jogos=int(input(f'Quantas  partidas {dicionario['nome']} jogou? '))

for partidas in range(1,jogos+1):
    gol=int(input(f'Quantos gols na partida {partidas}: '))
    gols.append(gol)
    partida_gol['partida']=jogos

partida_gol['gol']=gols
dicionario['gols']=gols
dicionario['total_gol']=sum(gols)

print('=-'*30)
print(dicionario)
print('=-'*30)

for k,v in dicionario.items():
    print(f'O {k} é igual: {v}')

print('=-'*30)

for i,v in enumerate(partida_gol):
    print(f'{i} e {v}')
