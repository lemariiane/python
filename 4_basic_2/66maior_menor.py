#sorteia 5 números entre 0 e 100 e mostra o maior e menor valor
import random
num_sorteados=(random.sample(range(0,100), 5))#.sample para escolher quantos números serão sorteados

print(num_sorteados)
print(f'O maior número foi {max(num_sorteados)}')
print(f'O menor número foi {min(num_sorteados)}')
