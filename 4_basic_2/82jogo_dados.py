import random

for i in range(1,5):
    dado=random.sample(range(1,6),1)
    print(f'Jogador{i} tirou {dado} no dado')