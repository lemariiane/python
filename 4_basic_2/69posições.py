#maior e meno valor na lista e suas posições
valores=[]
posicao_menor=[]
posicao_maior=[]
maior=menor=0
for i in range(0,5):
    valor=int(input(f'Digite um valor para a posição {i}: '))
    valores.append(valor)
    if i==0:
        maior=valor
        menor=valor
    if valor>maior:
        maior=valor
    if valor<menor:
        menor=valor

print(f'Você digitou os valores {sorted(valores)}')
for posicao,numero in enumerate(valores):
    if numero==maior:
        posicao_maior.append(posicao)
print(f'O maior valor digitado foi {maior} nas posições {posicao_maior}')
for posicao,numero in enumerate(valores):
    if numero==menor: 
        posicao_menor.append(posicao)
print(f'O menor valor digitado foi {menor} nas posições {posicao_menor}')
