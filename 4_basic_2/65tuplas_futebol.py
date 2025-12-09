#tuplas são imutáveis!
times = ( #tabela final de 2025
    "Flamengo", "Palmeiras", "Cruzeiro", "Mirassol",
    "Fluminense", "Botafogo", "Bahia", "São Paulo",
    "Grêmio", "Bragantino", "Atlético-MG", "Santos",
    "Corinthians", "Vasco da Gama", "EC Vitória", "Internacional",
    "Ceará SC", "Fortaleza", "Juventude", "Sport Recife"
)

print('='*40)
print(f'Todos os times são: {times[0:]}')
print('-'*90)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-'*90)
print(f'Os 4 últimos: {times[-4:]} ')
print('-'*90)
print(f'Times em ordem alfabética: {sorted(times)}')#só organiza para o print e não muda a ordem da tupla
print('-'*90)
print(f'O Grêmio está na {times.index('Grêmio')+1}°')
print('='*40)
