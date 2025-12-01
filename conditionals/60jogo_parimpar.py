#Jogo de par ou ímpar com o computador
from random import randint
from time import sleep
print('='*25)
print("JOGO: PAR OU ÍMPAR")
print('='*25)
cont_ganhou= 0 
resultado='X'

while True:
    print('-'*20) 
    while True:#Verifica se o valor é PAR OU ÍMPAR
        palpite=str(input('Par ou Ímpar? [P/I] ')).strip().upper()#Jogador irá dar o seu palpite 
        if palpite in ('P','I'):
            break
        palpite=str(input('Digite um valor válido: [P/I] ')).strip().upper()
    num=int(input('Aposte seu número: '))

    numcomp=randint(0,10) #'computador' irá apostar um número de 0 a 10

    print('CONTANDO...')
    sleep(2)

    print(f'Você jogou {num} e o computador jogou {numcomp}.')

    if (num+numcomp)%2==0: #Se o número for PAR
        print('O resultado deu PAR')
        resultado='P'
    else:
        print('O resultado deu ÍMPAR')
        resultado='I'

    if resultado==palpite: #Verifica se o resultado foi igual ao palpite do jogador
        print('Você GANHOU!!!')
        cont_ganhou+=1
    else:
        break

print('Você PERDEU!')
print('='*25)
if cont_ganhou==0:
    print('GAME OVER!!!! Você conseguiu ganhar NENHUMA rodada!')
elif cont_ganhou==1:
    print('GAME OVER! Você venceu só UMA rodada')
else:
    print(f'GAME OVER! Você venceu {cont_ganhou} vezes')
