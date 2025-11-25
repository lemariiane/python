soma=qnt=num=0

num=int(input('Digite o número [999 para parar]: '))

while num!=999:
    soma+=num
    qnt+=1
    num=int(input('Digite o número [999 para parar]: '))

print(f'Você digitou {qnt} e a soma entre eles é {soma}')
