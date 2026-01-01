lista=[]

for i in range (0,5):
    num=int(input('Digite um valor: '))
    if i ==0:
        lista.append(num)
    for n in lista:
        if num>n:
            print('O valor foi adicionado no final da lista')
            lista.append(num)
        elif num<n:
            print('O valor foi adicionado na posição 0')
            lista.insert(0,num)
print(lista)

print('Volte sempre!!')