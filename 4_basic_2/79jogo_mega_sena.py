#sorteando jogos para a mega sena
import random
print('_'*30)
print('JOGO NA MEGA SENA')
print('_'*30)
i=0
qnt=int(input('Quantos jogos você quer que eu sorteie? '))
print(f'----SORTEANDO {qnt} JOGOS----')

for i in range(1,qnt+1):
    sorteio = random.sample(range(1, 61), 6)#sorteando 6 números de 1 a 60 sem repetição
    print(f'JOGO {i}: {sorted(sorteio)})')
