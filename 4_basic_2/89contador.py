#exibe uma contagem do valor inicial até o final,
#ajustando automaticamente o sentido da contagem
#de acordo com a razão informada

from time import sleep
def contar(inicial,fim,razao):
    print('-='*20)
    if inicial>fim:
        fim-=1
    else:
        fim+=1

    for cont in range(inicial, fim, razao):
        print(f'{cont}', end=' ', flush=True)#flush para não mostrar só quando o buffer tiver cheio, e sim linha a linha
        sleep(0.5)
    print(' ')
        

contar(1,10,1)
contar(10,0,-2)

print('-='*20)

print('Agora é sua vez de personalizar a contagem!')
inicial=int(input('Ínicio: '))
fim=int(input('Fim: '))
razao=int(input('Razão: '))
contar(inicial,fim,razao)
