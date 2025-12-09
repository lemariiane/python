n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número: '))
n4=int(input('Digite o último número: '))
posicao3=0
numeros=(n1,n2,n3,n4)
pares=[]

for numero in numeros:
    if numero==3:
        posicao3=numeros.index(numero)+1 #o index: armazena a primeira ocorrência
    if numero%2==0:
        pares.append(numero)

if numeros.count(9)==0:
    print("Você não digitou o número 9.")
else:
    print(f'O número 9 foi repetido {numeros.count(9)} veze(s)!')

if posicao3==0:
    print('Você não digitou o número 3.')
else:
    print(f'O número 3 apareceu pela primeira vez na posição {posicao3}°!')

if len(pares)==0:
    print('Você não digitou nenhum número par.')
else:
    print(f'Os números pares foram {pares}.')
