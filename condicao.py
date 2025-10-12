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
# lado1=float(input("Digite o primeiro lado: "));
# lado2=float(input("Digite o segundo lado: "));
# lado3=float(input("Digite o terceiro lado: "));

# if lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1: #soma de quaisquer dos dois lados tem que ser maior que o terceiro
#     print("Esses lados FORMAM um triângulo!");
# else:
#     print("Essas medidas NÃO formam um triângulo!");

#aprovando um empréstimo
# valor_casa=float(input("Qual o valor da casa? R$"));
# salario=float(input("Qual o seu salário? R$"));
# tempo_ano=float(input("Em quantos anos pretende dividir? "));

# tempo_mes= tempo_ano*12; #valor mensal
# valor_prestacao=valor_casa/tempo_mes;

# print(f"Para pagar essa casa de R${valor_casa} em {tempo_ano} a prestação será de R${valor_prestacao:.2f}")

# if valor_prestacao < (salario*0.3): #no mínimo 30% do salário
#     print("PARABÉNS!! Seu empréstimo foi CONCEDIDO!");
# else:
#     print("Infelizmente seu empréstimo NÃO foi concedido!");

#conversor de números
# num=int(input("Digite um número inteiro: "));

# print('''Escolha uma das bases para conversão:
# [1] converter para BINÁRIO
# [2] converter para OCTAL
# [3] converter para HEXADECIMAL''');

# opcao=int(input('Sua opção: '));

# if opcao==1:
#     print(f"{num} convertido em BINÁRIO é {bin(num)[2:]}"); #Se não tivesse os [2:], no terminal apareceria: '0o55'
# elif opcao==2:
#     print(f"{num} convertido em OCTAL é {oct(num)}[2:]"); #[2:] é para pular as duas primeiras possições e aparecer só da 2 a diante (só números)
# elif opcao==3:
#     print(f"{num} convertido em HEXADECIMAL é {hex(num)[2:]}");
# else:
#     print("Digite uma opção válida!");

#Comparador de números
# print("Qual número é maior?");
# print("="*25);
# n1=int(input("Digite o primeiro valor: "));
# n2=int(input("Digite o segundo valor: "));

# if n1>n2: #se n1 é maior que n2
#     print("O primeiro valor é maior!");
# elif n2>n1:
#     print("O segundo valor é maior!");
# else:
#     print("Os valores são iguais");

#ALISTAMENTO MILITAR
from datetime import date;

print("ALISTAMENTO MILITAR OBRIGATÓRIO!"); #alistamento obrigatório: é no ano em que vc completa 18 anos
print("="*35);
ano_nasc=int(input("Digite o ano do seu nascimento: "));# ano de nascimento

ano_atual=date.today().year;
idade = ano_atual - ano_nasc ;

if idade > 18:
    print(f"Você tem {idade} anos e já deveria ter se alistado!");
    print(f"Você deveria ter se alistado a {idade-18} ano(s).");
    print(f"O ano do seu alistamento foi em {ano_atual-(idade-18)}."); 
elif idade < 18:
    print(f"Você tem {idade} anos e ainda não tem idade para se alistar!");
    print(f"Ainda falta(m) {18-idade} ano(s) para o seu alistamento.");
    print(f"Você deverá se alistar no ano de {ano_atual+(18-idade)}.");
else: #idade = 18
    print("Você deve se alistar IMEDIATAMENTE!");

