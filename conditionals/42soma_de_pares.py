#Soma dos núemros pares

soma=0;
for i in range(1,7):
    num=int(input(f'Digite o {i} valor: ')); #num de número
    if num % 2 == 0:
        soma+=num;
print(f'A soma dos pares é {soma}');
