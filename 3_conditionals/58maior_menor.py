continuar='S'
soma=qnt=maior=menor=0

while continuar in 'S':
    num=int(input('Digite um número: '))
    continuar=str(input('Quer contiuar? [S/N]: ')).strip().upper()#ignora os espaços em branco na frente e coloca para maiúsculo
    soma+=num

    if qnt == 0:
        maior = menor = num #maior e menor recebe o primeiro número digitado

    qnt+=1
    if num>maior:
        maior=num
    elif num<menor:
        menor=num

    while continuar not in ('S', 'N'):
        continuar = input('Valor inválido! Digite apenas S ou N: ').strip().upper()

print(f'Você digitou {qnt} números e média foi {soma/qnt:.2f}')
print(f'O maior valor é {maior} e o menor foi o {menor}')
