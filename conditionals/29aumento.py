#Aumento de salário
salario=float(input("Digite o salário do funcionário: R$"));

if salario<=1250: #salários abaixo ou iguais a 1250.
    aumento= salario*0.15;
    print(f"Com o aumento de 15% o novo salário é R${salario+aumento}");
else:
    aumento= salario*0.1;
    print(f"Com o aumento de 10% o novo salário é R${salario+aumento}");
