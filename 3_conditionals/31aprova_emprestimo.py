#aprovando um empréstimo. Valor da prestação tem que ser 30% ou menos do salário.

valor_casa=float(input("Qual o valor da casa? R$"));
salario=float(input("Qual o seu salário? R$"));
tempo_ano=float(input("Em quantos anos pretende dividir? "));

tempo_mes= tempo_ano*12; #valor mensal
valor_prestacao=valor_casa/tempo_mes;

print(f"Para pagar essa casa de R${valor_casa} em {tempo_ano} a prestação será de R${valor_prestacao:.2f}")

if valor_prestacao < (salario*0.3): #no mínimo 30% do salário
    print("PARABÉNS!! Seu empréstimo foi CONCEDIDO!");
else:
    print("Infelizmente seu empréstimo NÃO foi concedido!");
