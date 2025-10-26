import random;
from time import sleep;

print("Jogo de adivinhação");
print("Pensei em um número de 1 a 5. Você consegue adivinha-lo?");
print("="*15);
palpite= int(input("Qual seu palpite? ")); #usuário tenta advinhar, da o seu palpite

numsorteio=[1,2,3,4,5]; 
numsortido =random.choice(numsorteio); #computador "pensa" no número. random pega um núemro aleatório da lista numsorteio

print("PROCESSANDO...");
sleep(2);

if palpite not in numsorteio:
    print("Digite um número válido!");

elif palpite == numsortido:
    print("Parabéns, você me ganhou!!!");

else:
    print(f"Não foi dessa vez!!! O número que eu pensei foi {numsortido}.");