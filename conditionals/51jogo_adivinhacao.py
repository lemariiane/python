#Jogo de adivinhação com quantidades de tentativas
from random import randint;

print("---Jogo de adinhação---");
print("Pensei em número de 0 a 10");
print("Você consegue adivinhar? E em quantos palpites?");

acertou = False; 
qntpalpite=0;
numsortiado=randint(0,10);#computador pensando em um número

while not acertou:
    qntpalpite+=1;
    palpite=int(input("Qual o seu palpite? "));
    
    if numsortiado==palpite:
        acertou=True;
    else:
        if palpite<numsortiado:
            print('O número é MAIOR... Tente novamente');
        else:
            print('O número é MENOR... Tente novamente');


print(f'PARABÉNS!!! Você acertou o número {numsortiado} em {qntpalpite} tentativa(s).')
