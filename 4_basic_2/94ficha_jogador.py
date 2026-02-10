#Nome do jogador e seu número de gols no campeonato.
#Com valores nulos sendo aceitos
def jogador(nome=None,gols=None):
    gols=gols if gols else 0
    nome=nome if nome else '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome=str(input('Nome do jogador: ')).strip()
gols=str(input('Número de gols: ')).strip()
if not gols.isnumeric():
    gols=None
else:
    gols=int(gols)

print(jogador(nome,gols))
