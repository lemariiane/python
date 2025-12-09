#Usuário digita qual número da tabuada quer e o programa para quando ele digita um valor negativo
while True:
    num=int(input('Qual tabuada você gostaria de ver? '))
    if num<0:
        break
    else:
        for multiplicador in range(11):
            print(f'{num} X {multiplicador} = {num*multiplicador} ')
    print('-' * 30)

print('Fim do programa!')
