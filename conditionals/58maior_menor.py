continuar='S'
soma=i=maior=menor=0

while continuar=='S'or continuar=='s':
    num=int(input('Digite um número: '))
    continuar=str(input('Quer contiuar? [S/N]: '))
    soma+=num
    i+=1
    if num>maior:
        maior=num
    elif num>menor:
        menor=num

print(f'Você digitou {i} números e a soma é {soma} média foi {soma/i:.2f}')
print(f'O maior valor é {maior} e o menor foi o {menor}')
