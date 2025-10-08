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
# km=float(input("Quantos km são a sua viagem? "));

# print(f"Você está prestres a realizar uma viagem de {km}km")
# if km<200: #se a viagem for até 200km a taxa é 0.5, se não é 0.45
#     print(f"Sua viagem irá custar R${km*0.5}");
# else:
#     print(f"Sua viagem irá custar R${km*0.45}");

#esse ano é bissexto?
# from datetime import date;

# ano = int(input("Digite o ano: Coloque 0 para pegar o ano atual. "));
# if ano==0:
#     ano=date.today().year;
# if ano%4==0 and ano%100!=0 or 400==0:#bissexto: de 4 em 4 anos. 
# #Exeto em casos do número não for divissível por 100- mas quando ele é divissível  por 400,nesse caso, ele volta a ser bissexto. 
#      print(f"Esse ano de {ano} é bissexto");
# else:
#     print(f"O ano de {ano} não é bissexto!");

#Qual número é maior dos três?
# num1=int(input("Digite o primeiro número: "));
# num2=int(input("Digite o segundo número: "));
# num3=int(input("Digite o terceiro número: "));

# maior=max(num1,num2,num3); #função do python
# menor=min(num1,num2,num3);

# print(f"O maior é {maior} e o menor número é {menor}");

#Aumento de salário
# salario=float(input("Digite o salário do funcionário: R$"));

# if salario<=1250: #salários abaixo ou iguais a 1250.
#     aumento= salario*0.15;
#     print(f"Com o aumento de 15% o novo salário é R${salario+aumento}");
# else:
#     aumento= salario*0.1;
#     print(f"Com o aumento de 10% o novo salário é R${salario+aumento}");

#analisando o triângulo
