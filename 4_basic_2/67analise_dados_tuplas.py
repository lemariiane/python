n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
n3=int(input('Digite mais um número: '))
n4=int(input('Digite o último número: '))
cont=0
numeros=(n1,n2,n3,n4)
pares=[]

for numero in numeros:
    if numero==9:
        cont+=1
    if numero==3:
        posicao3=numeros.index(numero)+1 #o index: armazena a primeira ocorrência
    if numero%2==0:
        pares=[numero]

print(f'O número 9 foi repetido {cont} veze(s)')
print(f'O número 3 apareceu pela primeira vez na posição {posicao3}°')
print(f'Os números pares foram {pares}')
