import random;
from time import sleep;

# #Jogo de adivinhação
# print("Jogo de adivinhação");
# print("Pensei em um número de 1 a 5. Você consegue adivinha-lo?");
# print("="*15);
# palpite= int(input("Qual seu palpite? ")); #usuário tenta advinhar

# numsorteio=[1,2,3,4,5]; 
# numsortido =random.choice(numsorteio); #computador "pensa" no número

# print("PROCESSANDO...");
# sleep(2);

# if palpite not in numsorteio:
#     print("Digite um número válido!");

# elif palpite == numsortido:
#     print("Parabéns, você me ganhou!!!");

# else:
#     print(f"Não foi dessa vez!!! O número que eu pensei foi {numsortido}.");

#Multa de velocidade

# km=float(input("Qual a sua velocidade? "));

# if km<80: #80km/hr é o limite de velocidade
#     print("Pode seguir!!! Sua velocidade está dentro do permitido!");
# else:
#     print(f"Multado, você ultrapassou o limite de velocidade e recebeu uma multa de R${(km-80)*7}"); #7 reais para cada km acima do permitido

# print("Tenha um bom dia! Dirija com segurança!!");

#Par ou ímpar
# num=int(input("Digite qualquer número: "));

# if num%2==1:
#     print("Esse número é ímpar");
# else:
#     print("Esse número é par");

#Preço da viagem
km=float(input("Quantos km são a sua viagem? "));

print(f"Você está prestres a realizar uma viagem de {km}km")
if km<200:
    print(f"Sua viagem irá custar R${km*0.5}");
else:
    print(f"Sua viagem irá custar R${km*0.45}");