dicionario={}
gols=[]

dicionario['nome']=str(input('Nome jogador: '))
jogos=int(input(f'Quantas  partidas {dicionario['nome']} jogou? '))

for partidas in range(1,jogos+1):
    gol=int(input(f'Quantos gols na partida {partidas}: '))
    gols.append(gol)

dicionario['gols']=gols
dicionario['total_gol']=sum(gols)

print('=-'*30)
print(dicionario)
print('=-'*30)

for k,v in dicionario.items():
    print(f'O {k} é igual: {v}')

print('=-'*30)

for i,v in enumerate(dicionario['gols']):
    print(f'Na partida {i} o {dicionario['nome']} fez {v} gols!')
