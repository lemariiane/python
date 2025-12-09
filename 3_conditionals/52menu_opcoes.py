from time import sleep
num1=int(input('Primeiro valor: '))
num2=int(input('Segundo valor: '))

opcao=0

while opcao!=5:
    print('''[1] Somar
[2] Multiplicar 
[3] Maior
[4] Novos números 
[5] Sair do programa''')

    opcao=int(input('Qual é a sua opção? '))

    if opcao==1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif opcao==2:
        print(f'{num1} X {num2} = {num1*num2}')
    elif opcao==3:
        if num1>num2:
            print(f'O maior número é {num1}')
        else:
            print(f'O maior número é o {num2}')
    elif opcao==4:
        print('INFORME OS NOVOS NÚMEROS')
        num1=int(input('Primeiro valor: '))
        num2=int(input('Segundo valor: '))
    elif opcao==5:
        print('Finalizando...')
    else:
        print('Digite uma opção válida!')
    sleep(1.5)#demorar 1.5s para mostrar o menu novamente

print('Você saiu do programa!')
