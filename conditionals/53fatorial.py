#calcular o fatorial -> sem módulo factorial
num=int(input('Digite o número que deseja calcular o fatorial: '))
i=num
fatorial=1

while i>1:
    fatorial*=i
    i-=1
print(f'O resultado de {num}! = {fatorial}')
   