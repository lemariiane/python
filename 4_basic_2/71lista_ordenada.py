#Ordenando valores de uma lista sem o 'sorted' ou 'sort'
lista=[]

for i in range (0,5):
    num=int(input('Digite um valor: '))
    if i ==0 or num>lista[-1]:
        lista.append(num)
        print('O valor foi adicionado no final da lista...')
    else:
        pos=0
        while pos< len(lista):
            if num<=lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}...')
                break
            pos+=1

print(lista)
