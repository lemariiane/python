#analizando uma matriz
matriz=[]
soma_par=soma_coluna=maior_linha=0

for l in range (0,3):
    linha=[]
    for c in range (0,3):
        num=int(input(f'Digite o valor [{l}],[{c}]: '))
        if num %2==0:
            soma_par+=num
        linha.append(num)     
    matriz.append(linha)

for linha in matriz:
    print(linha)
    
for l in range (0,3):
    soma_coluna+=matriz[l][2]
for c in range (0,3):
    if c==0:
        maior_linha=matriz[1][c]
    elif matriz[1][c]>maior_linha:
        maior_linha=matriz[1][c]

print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_linha}')
