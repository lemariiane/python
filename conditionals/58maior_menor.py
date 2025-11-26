continuar='S'
soma=i=maior=menor=0

while continuar in 'Ss':
    num=int(input('Digite um número: '))
    continuar=str(input('Quer contiuar? [S/N]: '))
    soma+=num

    if i == 0:
        maior = menor = num #maior e menor recebe o primeiro número digitado

    i+=1
    if num>maior:
        maior=num
    elif num<menor:
        menor=num


print(f'Você digitou {i} números e média foi {soma/i:.2f}')
print(f'O maior valor é {maior} e o menor foi o {menor}')