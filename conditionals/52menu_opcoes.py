num1=int(print('Primeiro valor: '))
num2=int(print('Segundo valor: '))

print('[1] Somar' \
'[2] Multiplicar' \
'[3] Maior' \
'[4] Novos núemros' \
'[5] Sair do programa')

opcao=int(print('Qual é a sua opção'))

if opcao==1:
    print(f'A soma entre {num1} + {num2} = {num1+num2}')
