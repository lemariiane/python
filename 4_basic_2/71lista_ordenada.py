lista=[]

for i in range (0,5):
    num=int(input('Digite um valor: '))
    for numeros in lista:
        if num>numeros:
            print('O valor foi adicionado no final da lista')
            lista.append(num)
        elif num<numeros:
            print('O valor foi adicionado na posição 0')
            lista.insert(0,num)

print('Volte sempre!!')