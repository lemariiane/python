#separar em par e ímpar em uma lista só
i=num=0
numeros=[[],[]]
for i in range (0,7):
    num=int(input(f'Digite o {i}° valor: '))

    numeros.append(num)
    if num%2==0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    i+=1

print(f'Os pares foram: {sorted(numeros[0])}')
print(f'Os ímpares foram: {sorted(numeros[1])}')
