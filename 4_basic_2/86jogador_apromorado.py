jogadores=[]
cod=0
while True:
    dicionario={}
    gols=[]

    dicionario['nome']=str(input('Nome jogador: '))
    jogos=int(input(f'Quantas  partidas {dicionario['nome']} jogou? '))

    for partidas in range(1,jogos+1):
        gol=int(input(f'Quantos gols na partida {partidas}: '))
        gols.append(gol)
    
    cont=str(input('Deseja continuar? [S/N]')).strip().upper()
    while cont not in ('S','N'):
        cont=str(input('DADO INVÁLIDO! Digite apenas S/N: ')).strip().upper()
    
    dicionario['gols']=gols
    dicionario['total_gol']=sum(gols)
    dicionario['cod']=cod

    cod+=1

    jogadores.append(dicionario.copy())

    if cont=='N':
        break

print('=-'*30)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 60)
for j in jogadores:
    print(f'{j["cod"]:<4} {j["nome"]:<15} {str(j["gols"]):<15} {j["total_gol"]:<5}')
print('=-'*30)

while True:
    dado=int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    print(f'LEVANTAMENTO DO JOGADOR {jogadores[dado]['nome']}')