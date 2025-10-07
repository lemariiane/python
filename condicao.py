import random;

#Jogo de adivinhação
print("Jogo de adivinhação");
print("Pense em um número de 1 a 5");
print("===========================");
num= int(input("Qual seu palpite? "));

numsorteio=[1,2,3,4,5]; 
numsortido =random.choice(numsorteio);

if num not in numsorteio:
    print("Digite um número válido!");

elif num == numsortido:
    print("Parabéns você me ganhou!!!");

else:
    print(f"Não foi dessa vez!!! O número que eu pensei foi {numsortido}.");
