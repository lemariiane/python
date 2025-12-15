posicoes=(0,1,2,3,4)
pos_maior=[]
pos_menor=[]
lista=[]
print('-'*40)

for posicao in posicoes:
    num=int(input(f'Digite um valor para a posição {posicao}: '))
    if posicao==0:
        maior=num
        menor=num

    lista.append(num)

    if num>=maior:
        maior=num      
        pos_maior.append(posicao)

    elif menor>=num:
        menor=num
        pos_menor.append(posicao)
        

print('-'*40)
print(f'Você digitou os números {lista}')
print(f'O maior valor foi {maior} nas posições {pos_maior}')
print(f'O menor valor foi {menor} nas posições {pos_menor}')