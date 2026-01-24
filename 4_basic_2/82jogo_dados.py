import random
from operator import itemgetter

dicionario = {}

for i in range(1, 5):
    dado = random.randint(1, 6)
    print(f'Jogador {i} tirou {dado} no dado')
    dicionario[i] = dado

print('=-' * 20)
print('RANKING DOS JOGADORES')

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: jogador {v[0]} com {v[1]}')
